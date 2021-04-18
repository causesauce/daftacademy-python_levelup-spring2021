from fastapi import FastAPI, status, Response
from typing import Optional
import uvicorn
import hashlib

app = FastAPI()


@app.get("/auth", status_code=204)
def validate_password(password: str, password_hash: str, response: Response):
    if password_hash != hashlib.sha512(password.encode()).hexdigest():
        response.status_code = status.HTTP_401_UNAUTHORIZED


if __name__ == '__main__':
    uvicorn.run(app)
