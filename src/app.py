from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.init_db import Database
from services.query import query_rag
from models.document import QueryRequest

app = FastAPI()
db = Database()

@asynccontextmanager
async def lifespan(app: FastAPI):
    db.initialize()
    yield
    db.close()


app = FastAPI(lifespan=lifespan)


@app.post("/query")
async def query(request: QueryRequest):
    return await query_rag(request,db=db)
