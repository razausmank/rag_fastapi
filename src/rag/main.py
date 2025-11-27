from fastapi import FastAPI 
from src.rag.items.router import router as items_router


app = FastAPI()

app.include_router(items_router)


@app.get('/')
def root(): 
    return {"message" : "Hello World!"}


@app.get('/test')
def test(): 
    return { "message": "test" } 


@app.get('/test/{blah}')

def blah(blah): 
    return { "response": blah }
