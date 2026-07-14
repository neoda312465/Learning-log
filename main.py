from fastapi import FastAPI
from sqlmodel import SQLModel, Field, Session, create_engine, select

class Item(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    price: int

engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)

app = FastAPI()

@app.post("/items")
def create_item(item: Item):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item 
    
@app.get("/items")
def get_items():
    with Session(engine) as session:
        items = session.exec(select(Item)).all()
        return items
@app.get("/items/{item_id}")
def get_item(item_id: int):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        return item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        session.delete(item)
        session.commit()
        return {"message": "Item deleted successfully"}
