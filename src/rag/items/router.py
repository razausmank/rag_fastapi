from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.rag.common.deps import get_db
from .schemas import ItemRead

router = APIRouter(prefix="/items", tags=["users"])

@router.get("/", response_model=ItemRead)
def index(db: Session = Depends(get_db)): 
    return {
        "name" : "my first item", 
        "description" : "description of my first item"
    }