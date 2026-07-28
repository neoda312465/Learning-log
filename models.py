from sqlmodel import SQLModel, Field
from pydantic import field_validator
from typing import Optional
class Item(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    price: float

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