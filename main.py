from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.post("/method", status_code=201)
def method_post():
    return {"method": "POST"}


@app.get("/method", status_code=200)
def method_post():
    return {"method": "GET"}


@app.put("/method", status_code=200)
def method_post():
    return {"method": "PUT"}


@app.delete("/method", status_code=200)
def method_post():
    return {"method": "DELETE"}


@app.options("/method", status_code=200)
def method_post():
    return {"method": "OPTIONS"}


if __name__ == '__main__':
    uvicorn.run(app)
