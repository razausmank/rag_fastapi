from sqlalchemy.orm import Session
from .models import Document, Chunk
from .schemas import DocumentCreate, ChunkCreate


class RetrievalService:
    
    @staticmethod
    def create_document(db: Session, document: DocumentCreate) -> Document:
        """Create a new document"""
        db_document = Document(
            title=document.title,
            content=document.content
        )
        db.add(db_document)
        db.commit()
        db.refresh(db_document)
        return db_document
    
    @staticmethod
    def get_document(db: Session, document_id: int) -> Document:
        """Get a document by ID"""
        return db.query(Document).filter(Document.id == document_id).first()
    
    @staticmethod
    def get_all_documents(db: Session) -> list[Document]:
        """Get all documents"""
        return db.query(Document).all()
    
    @staticmethod
    def add_chunk(db: Session, chunk: ChunkCreate) -> Chunk:
        """Add a chunk to a document"""
        db_chunk = Chunk(
            document_id=chunk.document_id,
            chunk_text=chunk.chunk_text,
            embedding=chunk.embedding
        )
        db.add(db_chunk)
        db.commit()
        db.refresh(db_chunk)
        return db_chunk
    
    @staticmethod
    def get_chunks_by_document(db: Session, document_id: int) -> list[Chunk]:
        """Get all chunks for a document"""
        return db.query(Chunk).filter(Chunk.document_id == document_id).all()
    
    @staticmethod
    def simple_retrieve(db: Session, query: str) -> list[Chunk]:
        """Simple retrieval: search chunks by text match"""
        return db.query(Chunk).filter(
            Chunk.chunk_text.ilike(f"%{query}%")
        ).all()