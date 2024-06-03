from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from domain.post import post_CRUD, post_schema

router = APIRouter(
    prefix = "/api/post"
)

@router.get("/list", response_model=list[post_schema.Post])
def post_list(db: Session = Depends(get_db)):
    posts = post_CRUD.get_all_posts(db)
    return posts

@router.get("/detail/{post_id}", response_model=post_schema.Post)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = post_CRUD.get_specific_post(db, post_id)
    print(post)
    return post

@router.post("/add")
def make_post(post: post_schema.MakePost, db: Session = Depends(get_db)):
    post_CRUD.create_post(db, make_post=post)