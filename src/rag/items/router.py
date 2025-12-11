from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from rag.common.deps import get_db
from .schemas import ItemRead, ItemCreate
from .service import create_item
from .models import Item

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/", response_model=ItemRead)
def index(db: Session = Depends(get_db)): 
    return {
        "name" : "my first item", 
        "description" : "description of my first item"
    }

@router.post("/create", response_model = ItemRead)
def create_item_route(data: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db,data)

@router.get('/test') 
def test(db: Session = Depends(get_db)):
    try: 
        items = db.query(Item).all()
        return { 
            "status" : "connected" 
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
