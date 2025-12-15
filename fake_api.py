from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/api/login")
def login(data: dict):
    username = data.get("username")
    password = data.get("password")

    if username == "user1" and password == "pass1":
        return {"token": "abc123", "username": username}

    return JSONResponse({"error": "Invalid credentials"}, status_code=401)


@app.get("/api/profile")
def profile():
    return {
        "username": "user1",
        "email": "user1@example.com",
        "roles": ["admin", "user"]
    }
