from models import Post, User, Replies
from .post_schema import MakePost, PostUpdate
from sqlalchemy.orm import Session
from datetime import datetime


def get_all_posts(db: Session, skip: int = 0, page_size: int = 10, keyword: str = '', category_id: int = 0):
    posts = db.query(Post)
    if category_id != 0:
        posts = posts.filter(Post.category_id == category_id)
    if keyword:
        search = f"%{keyword}%"
        posts = db.query(Post).outerjoin(Replies).filter(Post.subject.ilike(search) | Post.content.ilike(search) | Replies.content.ilike(search))
        #filter

    total = posts.distinct().count()
    post_list = posts.offset(skip).limit(page_size).distinct().all()


    return total, post_list

def get_specific_post(db: Session, id):
    return db.query(Post).get(id)

def create_post(db: Session, make_post: MakePost, user: User):
    db_post = Post(
        subject = make_post.subject,
        content = make_post.content,
        replies = [],
        category_id = make_post.category_id,
        created_at = datetime.now(),
        modified_at = datetime.now(),
        user = user
        )
    db.add(db_post)
    db.commit()


def update_post(db: Session, db_post: Post, post_update: PostUpdate):
    db_post.subject = post_update.subject
    db_post.content = post_update.content
    db_post.category_id = post_update.category_id
    db_post.modified_at = datetime.now()
    db.add(db_post)
    db.commit()


def delete_post(db: Session, db_post: Post):
    db.delete(db_post)
    db.commit()

def like_post(db: Session, db_post: Post, db_user: User):
    db_post.voter.append(db_user)
    db.commit()

def unlike_post(db: Session, db_post: Post, db_user: User):
    db_post.voter.remove(db_user)
    db.commit()