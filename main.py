@app.get("/auth/")
def validate_password(password: str, password_hash: str, response: Response):
    normal_to_hashed = hashlib.sha512(password.encode()).hexdigest()
    response.status_code = 401
    if password_hash == normal_to_hashed:
        response.status_code = 204

    return response
