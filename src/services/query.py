import numpy as np
from fastapi import HTTPException
from src.services.embedding import get_embedding
from src.services.response import generate_response
from src.utils.similarity import cosine_similarity
from src.models.document import QueryRequest
from src.db.init_db import Database
import json


async def query_rag(request: QueryRequest, db: Database):
    query = request.query
    relevant_docs = retrieve_relevant_documents(query, db)
    if not relevant_docs:
        raise HTTPException(status_code=404, detail="No relevant documents found")
    response = generate_response(query, relevant_docs)
    return {"response": response}


def retrieve_relevant_documents(query, db: Database, top_k=3):
    document_box = db.get_document_box()  # Ensure document_box is initialized
    query_embedding = get_embedding(query)
    all_docs = document_box.get_all()
    similarities = [(doc, cosine_similarity(query_embedding, np.array(json.loads(doc.embedding)))) for doc in all_docs]
    similarities.sort(key=lambda x: x[1], reverse=True)
    return [doc for doc, _ in similarities[:top_k]]
