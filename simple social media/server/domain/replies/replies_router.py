from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from domain.post import post_CRUD, post_schema
from domain.replies import replies_schema, replies_CRUD
from domain.user.user_router import get_current_user
from starlette import status
import random
from models import User

router = APIRouter(
    prefix = "/api/reply"
)

@router.post("/add/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def add_reply(post_id: int, createreply: replies_schema.MakeReply, db: Session = Depends(get_db), curr_user: User = Depends(get_current_user)):
    post = post_CRUD.get_specific_post(db, id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Error retrieving post")
    
    replies_CRUD.create_reply(db, post=post, comment_create=createreply, user=curr_user)


@router.get("/detail/{reply_id}", response_model=replies_schema.GetReply)
def get_post(reply_id: int, db: Session = Depends(get_db)):
    reply = replies_CRUD.get_reply(db, id=reply_id)
    return reply


@router.put("/update", status_code=status.HTTP_204_NO_CONTENT)
def update_reply(change_reply: replies_schema.replyUpdate, db: Session = Depends(get_db), curr_user: User = Depends(get_current_user)):
    db_reply = replies_CRUD.get_reply(db, id=change_reply.id)
    if not db_reply:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Reply not available")
    if curr_user.id != db_reply.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="You are not permitted to change this reply")
    replies_CRUD.reply_update(db=db, db_reply=db_reply, replyupdate=change_reply) 


@router.get("/list", response_model=replies_schema.replyList)
def reply_list(post_id, db: Session = Depends(get_db), page: int = 0, page_size: int = 10):
    post = post_CRUD.get_specific_post(db, id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    print(page_size)
    total, replies = replies_CRUD.get_all_replies(db, skip=page*page_size, page_size=page_size, post_id=post_id)
    return {"total": total, "reply_list": replies}


@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
def delete(delete_reply: replies_schema.replyDelete, db: Session = Depends(get_db), curr_user: User = Depends(get_current_user)):
    reply = replies_CRUD.get_reply(db, id=delete_reply.id)
    if not reply:
        raise HTTPException(status_code=404, detail="Error retrieving reply")
    if curr_user.id != reply.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="You are not permitted to delete this reply")
    replies_CRUD.delete_reply(db, delete=reply)


@router.post("/like", status_code=status.HTTP_204_NO_CONTENT)
def reply_like(_reply: replies_schema.likeReply, db: Session = Depends(get_db), curr_user: User = Depends(get_current_user)):
    reply = replies_CRUD.get_reply(db, id=_reply.id)
    if not reply:
        raise HTTPException(status_code=404, detail="Error retrieving reply")
    if curr_user in reply.voter:
        replies_CRUD.unlike_reply(db, db_reply=reply, db_user=curr_user)
    else:
        replies_CRUD.like_reply(db, db_reply=reply, db_user=curr_user)


# @router.post("/testcommentspam", status_code=status.HTTP_204_NO_CONTENT)
# def spamcomments(post_id, db: Session = Depends(get_db), curr_user: User = Depends(get_current_user)):
#     post = post_CRUD.get_specific_post(db, id=post_id)
#     if not post:
#         raise HTTPException(status_code=404, detail="Error retrieving post")
#     test = replies_schema.MakeReply
#     adj = [
#     "Enigmatic",
#     "Vibrant",
#     "Tranquil",
#     "Curious",
#     "Gloomy",
#     "Whimsical",
#     "Radiant",
#     "Fragrant",
#     "Jagged",
#     "Serene",
#     "Luminous",
#     "Agile",
#     "Melodic",
#     "Ancient",
#     "Silky",
#     "Mysterious",
#     "Dazzling",
#     "Rustic",
#     "Gleeful",
#     "Intrepid"]
#     noun = [
#     "Apple",
#     "Ocean",
#     "Bicycle",
#     "Mountain",
#     "Robot",
#     "Lantern",
#     "Puzzle",
#     "Castle",
#     "Thunder",
#     "Journal",
#     "Guitar",
#     "Starfish",
#     "Whisper",
#     "Marshmallow",
#     "Volcano",
#     "Library",
#     "Rainbow",
#     "Octopus",
#     "Tapestry",
#     "Mirror"]
#     for i in range(100):
#         test.content = adj[random.randint(0, 19)] + " " + noun[random.randint(0, 19)]
#         replies_CRUD.create_reply(db, post=post, comment_create=test, user=curr_user)
