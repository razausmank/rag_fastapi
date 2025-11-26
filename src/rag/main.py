from fastapi import FastAPI 

app = FastAPI()


@app.get('/')
def root(): 
    return {"message" : "Hello World!"}


@app.get('/test')
def test(): 
    return { "message": "test" } 


@app.get('/test/{blah}')

def blah(blah): 
    return { "response": blah }
