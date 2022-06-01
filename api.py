import uvicorn
from fastapi import FastAPI
from main import score

app = FastAPI()

@app.post("/input")
async def input(text1 : str = Form(), text2 : str = Form()):
    return ("similarity_score = ", score(text1, text2))

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)
