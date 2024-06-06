import json
from transformers import AutoModel, AutoTokenizer
from src.db.init_db import Database
from src.db.schema.document import Document

embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"
embedding_tokenizer = AutoTokenizer.from_pretrained(embedding_model_name)
embedding_model = AutoModel.from_pretrained(embedding_model_name)


def get_embedding(text):
    inputs = embedding_tokenizer(text, return_tensors="pt")
    outputs = embedding_model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach().numpy().flatten()


def store_documents(db: Database, json_file_path: str):
    document_box = db.get_document_box()  # Ensure document_box is initialized

    with open(json_file_path, 'r') as file:
        documents = json.load(file)

    for document in documents:
        text = document["text"]
        embedding = json.dumps(get_embedding(text).tolist())  # Convert numpy array to JSON string
        doc = Document(text=text, embedding=embedding)
        document_box.put(doc)
    print("Documents stored")
