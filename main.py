from fastapi import FastAPI, status, Response, Request
import uvicorn
import hashlib

app = FastAPI()


#
# @app.get("/auth/")
# def validate_password(password: str, password_hash: str, response: Response):
#     normal_to_hashed = hashlib.sha512(password.encode()).hexdigest()
#     response.status_code = 401
#     if password_hash == normal_to_hashed and password is not None and password_hash is not None and password != '' and \
#             password_hash != '':
#         response.status_code = 204
#
#     return response


@app.get("/auth")
def validate_password2(request: Request, response: Response):
    response.status_code = 401
    if request.query_params == '' or request.query_params is None:
        a = str(request.query_params).split("&")
        password = a[0].split("=")[1]
        password_hash = a[1].split("=")[1]
        normal_to_hashed = hashlib.sha512(password.encode()).hexdigest()

        if password_hash == normal_to_hashed and password is not None and password_hash is not None \
                and password != '' and \
                password_hash != '':
            
            response.status_code = 204

    return response


if __name__ == '__main__':
    uvicorn.run(app)
