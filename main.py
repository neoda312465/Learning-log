from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Hello, Neo!"}

class person(BaseModel):
    name:str
    age: int
@app.post("/greet")
def greet(person: person):
    return{"message": f"Hello {person.name} bhai, you are {person.age} years old! Wow, you are young!"}

@app.get("/user/{user_id}")
def get_user(user_id: int, verbose: bool = False):
    if verbose:
        return{"user_id": user_id, "detail": f"Full information about user {user_id}"}
    return {"user_id": user_id}