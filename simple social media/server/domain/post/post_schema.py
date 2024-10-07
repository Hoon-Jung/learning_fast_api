from pydantic import BaseModel, field_validator
import datetime
from domain.replies.replies_schema import GetReply
from domain.user.user_schema import UserShow
from domain.category.category_schema import Category

class Post(BaseModel):
    id: int
    subject: str
    content: str
    replies: list[GetReply]
    created_at: datetime.datetime
    modified_at: datetime.datetime | None = None
    user: UserShow | None
    voter: list[UserShow] = []
    category: Category


class MakePost(BaseModel):
    subject: str
    content: str
    category_id: int

    @field_validator("subject", "content")
    def not_empty(cls, v):
        if not v:
            raise ValueError("Missing a subject/content")
        return v
    

class PostList(BaseModel):
    total: int=0
    posts: list[Post]

class PostUpdate(MakePost):
    post_id: int

class PostDelete(BaseModel):
    post_id: int

class PostLike(BaseModel):
    post_id: int