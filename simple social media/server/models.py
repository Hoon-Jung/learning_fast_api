from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship

from database import Base

post_voter = Table(
    'post_voter',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('post_id', Integer, ForeignKey('post.id'), primary_key=True),
)

reply_voter = Table(
    'comment_voter',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('comment_id', Integer, ForeignKey('replies.id'), primary_key=True),
)

class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True)
    subject = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    user = relationship("User", backref="posting_user")
    modified_at = Column(DateTime, nullable=True)
    voter = relationship("User", secondary=post_voter, backref="post_voters")




class Replies(Base):
    __tablename__ = "replies"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"))
    connected_post = relationship("Post", backref="replies")
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    user = relationship("User", backref="replied_user")
    modified_at = Column(DateTime, nullable=True)
    voter = relationship("User", secondary=reply_voter, backref="reply_voters")


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(60), nullable=False)
    email = Column(String(254), unique=True, nullable=False)