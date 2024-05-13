from pydantic import BaseModel
import datetime
from domain.replies.replies_schema import GetReply

class Post(BaseModel):
    id: int
    subject: str
    content: str
    comments: list[GetReply]
    created_at: datetime.datetime
