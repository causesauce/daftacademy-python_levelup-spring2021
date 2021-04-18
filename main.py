from fastapi import FastAPI, status, Response
import uvicorn
import hashlib

app = FastAPI()


@app.get("/auth")
def validate_password(password: str, password_hash: str, response: Response):

    normal_to_hashed = hashlib.sha512(password.encode()).hexdigest()
    response.status_code = 222#status.HTTP_220_UNAUTHORIZED
    if password_hash == normal_to_hashed and password is not None and password_hash is not None and password != '' and password_hash != '':
        response.status_code = 222#status.HTTP_204_NO_CONTENT

    return response


if __name__ == '__main__':
    uvicorn.run(app)
