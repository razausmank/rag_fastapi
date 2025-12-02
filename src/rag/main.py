from fastapi import FastAPI 
from src.rag.items.router import router as items_router
from src.rag.core.db import Base, engine
from src.rag.items.models import Item 

app = FastAPI()

app.include_router(items_router)

Base.metadata.create_all(bind=engine)

@app.get('/')
def root(): 
    return {"message" : "Hello World!"}


@app.get('/test')
def test(): 
    return { "message": "test" } 


@app.get('/test/{blah}')

def blah(blah): 
    return { "response": blah }
