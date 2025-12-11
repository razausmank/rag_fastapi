from fastapi import FastAPI 
from rag.items.router import router as items_router
from rag.retrieval.router import router as retrieval_router
from rag.core.db import Base, engine
from rag.items.models import Item 

app = FastAPI()

app.include_router(items_router)
app.include_router(retrieval_router)

Base.metadata.create_all(bind=engine)

@app.get('/')
def root(): 
    return {"message" : "Hello World!"}


@app.get('/test')
def test(): 
    return { "message": "test" } 


@app.get('/test/{blah}')

def blah(blah: str) -> dict:
    return { "response": blah }
