from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from domain.post import post_CRUD, post_schema
from domain.replies import replies_schema, replies_CRUD
from starlette import status

router = APIRouter(
    prefix = "/api/reply"
)

@router.post("/add/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def add_reply(post_id: int, createreply: replies_schema.MakeReply, db: Session = Depends(get_db)):
    post = post_CRUD.get_specific_post(db, id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Error retrieving post")
    
    replies_CRUD.create_reply(db, post=post, comment_create=createreply)