from sqlmodel import SQLModel, Field
from pydantic import field_validator
from typing import Optional
class Item(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    price: float
    user_id: int = Field(default=None, foreign_key="user.id")
class ItemCreate(SQLModel):
    name: str
    price: float
    @field_validator("price")
    @classmethod
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("Price must be greater than 0")
        return value

class ItemUpdate(SQLModel):
    name: Optional[str] = None
    price: Optional[float] = None

    @field_validator("price")
    @classmethod
    def price_must_be_positive(cls, value):
        if value is not None and value <= 0:
            raise ValueError("Price must be greater than 0")
        return value

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str
    email: str = Field(default=None, unique=True)
    hashed_password: str

class UserCreate(SQLModel):
    username: str 
    email: str
    password: str

    @field_validator("password")
    @classmethod
    def password_must_be_strong(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return value

class UserLogin(SQLModel):
    email: str
    password: str