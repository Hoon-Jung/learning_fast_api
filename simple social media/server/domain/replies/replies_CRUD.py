from models import Post, Replies
from sqlalchemy.orm import Session
from .replies_schema import MakeReply
from datetime import datetime


def create_reply(db: Session, post: Post, comment_create: MakeReply):
    db_comment = Replies(
        content = comment_create.content,
        connected_post = post,
        created_at = datetime.now())
    
    db.add(db_comment)
    db.commit()