# main.py

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


uvicorn.run(app)
