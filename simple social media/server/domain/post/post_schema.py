from pydantic import BaseModel
import datetime
from domain.replies.replies_schema import GetReply

class Post(BaseModel):
    id: int
    subject: str
    content: str
<<<<<<< HEAD
    comments: list[GetReply]
=======
    replies: list[GetReply]
>>>>>>> d2012c2 (Debugged everything (only UI is left))
    created_at: datetime.datetime
