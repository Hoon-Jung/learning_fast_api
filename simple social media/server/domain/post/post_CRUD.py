from models import Post
from .post_schema import MakePost
from sqlalchemy.orm import Session
from datetime import datetime


def get_all_posts(db: Session, skip: int = 0, page_size: int = 10):
    posts = db.query(Post).order_by(Post.created_at.desc())

    total = posts.count()

    current_posts = posts.offset(skip).limit(page_size).all()

    return total, current_posts

def get_specific_post(db: Session, id):
    return db.query(Post).get(id)

def create_post(db: Session, make_post: MakePost):
    db_post = Post(
        subject = make_post.subject,
        content = make_post.content,
        replies = [],
        created_at = datetime.now()
    )
    db.add(db_post)
    db.commit()