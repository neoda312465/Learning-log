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