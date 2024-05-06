from pydantic import BaseModel
import datetime

class Post(BaseModel):
    id: int
    subject: str
    content: str
    created_at: datetime.datetime
