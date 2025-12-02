from sqlalchemy.orm import Session 
from .models import Item 
from .schemas import ItemCreate

def create_item(db:Session, data:ItemCreate):
    item = Item(**data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)

    return item 