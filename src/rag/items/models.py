from sqlalchemy import Column, Integer, String
from src.rag.core.db import engine 
from src.rag.core.db import Base

class Item(Base): 

    __tablename__ = "items"

    id = Column(Integer , primary_key=True , index=True)
    name = Column(String, nullable=True) 
    description = Column(String)