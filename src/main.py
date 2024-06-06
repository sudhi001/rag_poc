import os

from src.db.init_db import Database
from services.embedding import store_documents


# Set environment variable to disable tokenizer parallelism warning
os.environ["TOKENIZERS_PARALLELISM"] = "false"

if __name__ == "__main__":
    db = Database()
    db.initialize()
    json_file_path = "../data/documents.json"
    store_documents(db,json_file_path)
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
