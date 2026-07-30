from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session, select
from database import engine, init_db
from models import Item, ItemCreate, ItemUpdate, User, UserCreate, UserLogin
from auth import pwd_context, create_access_token, get_current_user_id

app = FastAPI()
init_db()
@app.post("/items")
def create_item(item: ItemCreate, user_id: int = Depends(get_current_user_id)):
    db_Item = Item(name=item.name, price=item.price, user_id=user_id)
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
def delete_item(item_id: int, user_id: int = Depends(get_current_user_id)):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        if item.user_id != user_id:
            raise HTTPException(status_code=403, detail="Not authorized to delete this item")
        session.delete(item)
        session.commit()
        return {"message": "Item deleted successfully"}

@app.put("/items/{item_id}")
def update_item(item_id: int, item_update: ItemUpdate, user_id: int = Depends(get_current_user_id)):
    with Session(engine) as session:
        db_item = session.get(Item, item_id)
        if not db_item:
            raise HTTPException(status_code=404, detail="Item not found")
        
        item_data = item_update.model_dump(exclude_unset=True)
        for key, value in item_data.items():
            setattr(db_item, key, value)
        session.add(db_item)
        session.commit()
        return db_item

@app.post("/signup")
def signup(user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password, username=user.username)
    with Session(engine) as session:
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user

@app.post("/login")
def login(user: UserLogin):
    with Session(engine) as session:
        db_user = session.exec(select(User).where(User.email == user.email)).first()
        if not db_user:
            raise HTTPException(status_code=400, detail="Invalid email or password")
        if not pwd_context.verify(user.password, db_user.hashed_password):
            raise HTTPException(status_code=400, detail="Invalid email or password")
        some_token =create_access_token({"user_id": db_user.id})
        return {"access_token":some_token, "token_type": "bearer"}
