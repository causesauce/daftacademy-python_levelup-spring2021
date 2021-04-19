from fastapi import FastAPI, status, Response, Request
import uvicorn
import hashlib

app = FastAPI()


# @app.get("/auth/")
# def validate_password(password: str, password_hash: str, response: Response):
#     normal_to_hashed = hashlib.sha512(password.encode()).hexdigest()
#     response.status_code = 401
#     if password_hash == normal_to_hashed:
#         response.status_code = 204
#
#     return response


# @app.get("/auth")
# def validate_password(request: Request, password: str, password_hash: str, response: Response):
#
#     response.status_code = 401
#
#
#
#     print(password)
#     print(password_hash)
# if request.query_params != '' or request.query_params is not None:
#     a = str(request.query_params).split("&")
#     if len(a) < 2:
#         return response
# password2 = a[0].split("=")[1]
# password_hash2 = a[1].split("=")[1]
# print(password2 == password)
# print(password2)
# print(password)
# normal_to_hashed = hashlib.sha512(password.encode()).hexdigest()
# response.status_code = status.HTTP_401_UNAUTHORIZED
# if password_hash == normal_to_hashed and password is not None and password_hash is not None and password != '' and password_hash != '':
#     response.status_code = status.HTTP_204_NO_CONTENT
#
# return response


@app.get("/auth")
def validate_password2(request: Request, response: Response):
    response.status_code = 401
    params_values = list(request.query_params.values())
    if len(params_values) < 2:
        return
    password = params_values[0]
    password_hash = params_values[1]
    if password is None or password_hash is None or password == '' or password_hash == '':
        return response
    normal_to_hashed = hashlib.sha512(password.encode()).hexdigest()
    print(password)
    print(password_hash)
    print(normal_to_hashed)
    if password_hash == normal_to_hashed:
        response.status_code = 204

    return response


if __name__ == '__main__':
    uvicorn.run(app)
