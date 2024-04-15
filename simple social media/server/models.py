from sqlalchemy import Column, Integer, String, Text, DateTime

from database import Base


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True)
    subject = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)


