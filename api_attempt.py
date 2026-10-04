from fastapi import FastAPI

app = FastAPI()

# 1️⃣ Root endpoint
@app.get("/")
def home():
    return {"message": "FastAPI is running successfully!"}

# 2️⃣ Simple JSON endpoint
@app.get("/hello")
def hello():
    return {"greet": "Hello Himadri!", "status": "success"}

# 3️⃣ Endpoint with path parameter
@app.get("/square/{number}")
def square(number: int):
    return {"number": number, "square": number * number}

# 4️⃣ Endpoint with query parameters
@app.get("/add")
def add(a: int, b: int):
    return {"a": a, "b": b, "sum": a + b}

# 5️⃣ Endpoint returning structured JSON
@app.get("/user/{name}")
def user_info(name: str, age: int = 30):
    return {
        "name": name,
        "age": age,
        "message": f"User {name} is {age} years old."
    }

# 6️⃣ Endpoint returning a list of items
@app.get("/items")
def items():
    return {
        "items": [
            {"id": 1, "name": "Laptop", "price": 55000},
            {"id": 2, "name": "Mouse", "price": 1200},
            {"id": 3, "name": "Keyboard", "price": 1800},
        ]
    }

# 7️⃣ Endpoint returning nested JSON
@app.get("/profile")
def profile():
    return {
        "user": {
            "name": "Himadri",
            "location": "Thane",
            "skills": ["Python", "FastAPI", "Playwright", "Automation"]
        },
        "status": "active"
    }
