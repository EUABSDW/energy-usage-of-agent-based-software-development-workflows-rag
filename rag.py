from fastapi import FastAPI
from pydantic import BaseModel

from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, TextLoader

import os

app = FastAPI()

DB_DIR = "db"
DOCS_DIR = "docs"

embeddings = OllamaEmbeddings(model="nomic-embed-text")

llm = ChatOllama(model="llama3")

# -------------------------
# CARGAR O CREAR BASE
# -------------------------
if os.path.exists(DB_DIR) and os.listdir(DB_DIR):
    db = Chroma(
        persist_directory=DB_DIR,
        embedding_function=embeddings
    )
else:
    docs = []

    for file in os.listdir(DOCS_DIR):
        path = os.path.join(DOCS_DIR, file)

        if file.endswith(".pdf"):
            loader = PyPDFLoader(path)
            docs.extend(loader.load())

        elif file.endswith(".txt"):
            loader = TextLoader(path, encoding="utf-8")
            docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)

    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=DB_DIR
    )

    db.persist()

# -------------------------
# API
# -------------------------
class Query(BaseModel):
    question: str

@app.post("/chat")
def chat(query: Query):

    docs = db.similarity_search(query.question, k=4)
    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
Usa SOLO el contexto para responder.

Contexto:
{context}

Pregunta:
{query.question}
"""

    response = llm.invoke(prompt)

    return {"answer": response.content}
