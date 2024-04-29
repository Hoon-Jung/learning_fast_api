from sqlalchemy import Column, Integer, String, Text, DateTime

from database import Base


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True)
    schoolname = Column(Text, nullable=False)
    webaddress = Column(Text, nullable=False)

