import uvicorn
from fastapi import FastAPI, Form
from main import score

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/input/")
def input(text1 : str = Form(), text2 : str = Form()):
    return {"similarity_score = ": score(text1, text2)}

if __name__ == "__main__":
    uvicorn.run(app)
