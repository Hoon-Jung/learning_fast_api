from models import Post, Replies, User
from sqlalchemy.orm import Session
from .replies_schema import MakeReply, replyUpdate
from datetime import datetime


def create_reply(db: Session, post: Post, comment_create: MakeReply, user: User):
    db_comment = Replies(
        content = comment_create.content,
        connected_post = post,
        created_at = datetime.now(),
        user = user)
    
    db.add(db_comment)
    db.commit()


def get_reply(db: Session, id):
    return db.query(Replies).get(id)


def reply_update(db: Session, db_reply: Replies, replyupdate: replyUpdate):
    db_reply.content = replyupdate.content
    db_reply.modified_at = datetime.now()
    db.add(db_reply)
    db.commit()


def delete_reply(db: Session, delete: Replies):
    db.delete(delete)
    db.commit()


def like_reply(db: Session, db_reply: Replies, db_user: User):
    db_reply.voter.append(db_user)
    db.commit()


def unlike_reply(db: Session, db_reply: Replies, db_user: User):
    db_reply.voter.remove(db_user)
    db.commit()