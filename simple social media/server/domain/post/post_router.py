from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from domain.post import post_CRUD, post_schema
from domain.user.user_router import get_current_user
from models import User

router = APIRouter(
    prefix = "/api/post"
)

@router.get("/list", response_model=post_schema.PostList)
def post_list(db: Session = Depends(get_db), page: int = 0, page_size: int = 10, keyword: str = ''):
    total, posts = post_CRUD.get_all_posts(db, skip=page*page_size, page_size=page_size, keyword=keyword)
    return {"total": total, "posts": posts}

@router.get("/detail/{post_id}", response_model=post_schema.Post)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = post_CRUD.get_specific_post(db, post_id)
    return post

@router.post("/add", status_code=status.HTTP_204_NO_CONTENT)
def make_post(post: post_schema.MakePost, db: Session = Depends(get_db), curr_user: User = Depends(get_current_user)):
    post_CRUD.create_post(db, make_post=post, user=curr_user)

@router.put("/update", status_code=status.HTTP_204_NO_CONTENT)
def update_post(change_post: post_schema.PostUpdate, db: Session = Depends(get_db), curr_user: User = Depends(get_current_user)):
    db_post = post_CRUD.get_specific_post(db, id=change_post.post_id)
    if not db_post:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Post not available")
    if curr_user.id != db_post.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="You are not permitted to change this post")
    post_CRUD.update_post(db=db, db_post=db_post, post_update=change_post)    


@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
def post_delete(delete_post: post_schema.PostDelete, db: Session = Depends(get_db), curr_user: User = Depends(get_current_user)):
    db_post = post_CRUD.get_specific_post(db, id=delete_post.post_id)
    if not db_post:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Post not available")
    if curr_user.id != db_post.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="You are not permitted to delete this post")
    post_CRUD.delete_post(db=db, db_post=db_post)


@router.post("/like", status_code=status.HTTP_204_NO_CONTENT)
def post_like(_post: post_schema.PostLike, db: Session = Depends(get_db), curr_user: User = Depends(get_current_user)):
    
    db_post = post_CRUD.get_specific_post(db, id=_post.post_id)
    if not db_post:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Post not available")
    if curr_user in db_post.voter:
        post_CRUD.unlike_post(db=db, db_post=db_post, db_user=curr_user)
    else:
        post_CRUD.like_post(db=db, db_post=db_post, db_user=curr_user)
    
    

    