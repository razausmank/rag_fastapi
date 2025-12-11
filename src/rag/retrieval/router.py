from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from rag.common.deps import get_db
from .service import RetrievalService
from .schemas import DocumentCreate, DocumentResponse, ChunkCreate, ChunkResponse

router = APIRouter(prefix="/retrieval", tags=["retrieval"])


@router.post("/documents", response_model=DocumentResponse)
def create_document(document: DocumentCreate, db: Session = Depends(get_db)):
    """Create a new document"""
    return RetrievalService.create_document(db, document)


@router.get("/documents/{document_id}", response_model=DocumentResponse)
def get_document(document_id: int, db: Session = Depends(get_db)):
    """Get a document by ID with all its chunks"""
    document = RetrievalService.get_document(db, document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document


@router.get("/documents", response_model=list[DocumentResponse])
def get_all_documents(db: Session = Depends(get_db)):
    """Get all documents"""
    return RetrievalService.get_all_documents(db)


@router.post("/chunks", response_model=ChunkResponse)
def add_chunk(chunk: ChunkCreate, db: Session = Depends(get_db)):
    """Add a chunk to a document"""
    return RetrievalService.add_chunk(db, chunk)


@router.post("/search")
def search(query: str, db: Session = Depends(get_db)):
    """Simple text-based search"""
    results = RetrievalService.simple_retrieve(db, query)
    return {"query": query, "results": results}