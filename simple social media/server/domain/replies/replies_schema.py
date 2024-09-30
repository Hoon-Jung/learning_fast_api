from pydantic import BaseModel, field_validator
import datetime
from domain.user.user_schema import UserShow
from models import Replies

class MakeReply(BaseModel):
    content: str

    @field_validator("content")
    def not_empty(cls, v):
        if not v:
            raise ValueError("Content value is empty")
        return v


class GetReply(BaseModel):
    id: int
    content: str
    user: UserShow | None
    post_id: int
    created_at: datetime.datetime
    voter: list[UserShow] = []
    voter_count: int


class replyUpdate(MakeReply):
    id: int

class replyDelete(BaseModel):
    id: int

class likeReply(BaseModel):
    id: int

class replyList(BaseModel):
    total: int
    reply_list: list[GetReply] = []

