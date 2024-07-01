from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from domain.post import post_CRUD, post_schema

router = APIRouter(
    prefix = "/api/post"
)

@router.get("/list", response_model=post_schema.PostList)
def post_list(db: Session = Depends(get_db), page: int = 0, page_size: int = 10):
    total, posts = post_CRUD.get_all_posts(db, skip=page*page_size, page_size=page_size)
    return {"total": total, "posts": posts}

@router.get("/detail/{post_id}", response_model=post_schema.Post)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = post_CRUD.get_specific_post(db, post_id)
    print(post)
    return post

@router.post("/add", status_code=status.HTTP_204_NO_CONTENT)
def make_post(post: post_schema.MakePost, db: Session = Depends(get_db)):
    post_CRUD.create_post(db, make_post=post)