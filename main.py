from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select
from database import engine, init_db
from models import Item, ItemCreate

app = FastAPI()
init_db()
@app.post("/items")
def create_item(item: ItemCreate):
    db_Item = Item(name=item.name, price=item.price)
    with Session(engine) as session:
        session.add(db_Item)
        session.commit()
        session.refresh(db_Item)
        return db_Item

@app.get("/items")
def get_items():
    with Session(engine) as session:
        items = session.exec(select(Item)).all()
        return items
@app.get("/items/{item_id}")
def get_item(item_id: int):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        return item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        session.delete(item)
        session.commit()
        return {"message": "Item deleted successfully"}
