from fastapi import APIRouter, Depends
from models import Post
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(
    prefix = "/api/post"
)

@router.get("/list")
def post_list(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return posts

# @router.get("/1")

    return posts