from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class ChunkBase(BaseModel):
    chunk_text: str
    embedding: Optional[str] = None


class ChunkCreate(ChunkBase):
    document_id: int


class ChunkResponse(ChunkBase):
    id: int
    document_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class DocumentBase(BaseModel):
    title: str
    content: str


class DocumentCreate(DocumentBase):
    pass


class DocumentResponse(DocumentBase):
    id: int
    created_at: datetime
    chunks: List[ChunkResponse] = []

    class Config:
        from_attributes = True