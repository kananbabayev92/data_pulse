from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get("/")
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

@router.post("/")
async def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    db_post = models.Post(**post.dict())  # Yeni SQLAlchemy obyekt yaradılır
    db.add(db_post)                       # Verilənlər bazasına əlavə olunur
    db.commit()                           # Dəyişikliklər saxlanılır
    db.refresh(db_post)                   # Obyekti yeniləyir (ID və s. dolur)
    return db_post
