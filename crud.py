from sqlalchemy.orm import Session
from models import Author, Book
from schemas import AuthorCreate, BookCreate
from typing import Optional


def create_author(db: Session, author: AuthorCreate):
    db_author = Author(name=author.name, bio=author.bio)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Author).offset(skip).limit(limit).all()


def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()


def create_book(db: Session, book: BookCreate, author_id: int):
    db_book = Book(title=book.title, summary=book.summary, publication_date=book.publication_date, author_id=author_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_books(db: Session, skip: int = 0, limit: int = 10, author_id: Optional[int] = None):
    query = db.query(Book).offset(skip).limit(limit)
    if author_id:
        query = query.filter(Book.author_id == author_id)
    return query.all()
