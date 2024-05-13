from pydantic import BaseModel, field_validator
import datetime

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
    created_at: datetime.datetime