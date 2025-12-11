from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from rag.core.db import Base

class Document(Base): 

    __tablename__ = "documents"

    id = Column(Integer , primary_key=True , index=True)
    title = Column(String, nullable=False) 
    content = Column(String, nullable=False)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    chunks = relationship("Chunk", back_populates="document")

class Chunk(Base):  

    __tablename__ = "chunks"

    id = Column(Integer , primary_key=True , index=True)
    document_id = Column(Integer, ForeignKey('documents.id'), nullable=False)
    chunk_text = Column(Text, nullable=False)
    embedding = Column(String, nullable=True)  # Assuming embedding is stored as a string

    document = relationship("Document", back_populates="chunks")
    
    