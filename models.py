from sqlmodel import SQLModel, Field
from pydantic import field_validator

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