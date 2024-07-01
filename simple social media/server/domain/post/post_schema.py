from pydantic import BaseModel, field_validator
import datetime
from domain.replies.replies_schema import GetReply

class Post(BaseModel):
    id: int
    subject: str
    content: str
    replies: list[GetReply]
    created_at: datetime.datetime


class MakePost(BaseModel):
    subject: str
    content: str

    @field_validator("subject", "content")
    def not_empty(cls, v):
        if not v:
            raise ValueError("Missing a subject/content")
        return v
    

class PostList(BaseModel):
    total: int=0
    posts: list[Post]