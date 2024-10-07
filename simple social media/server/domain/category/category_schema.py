from pydantic import BaseModel

class Category(BaseModel):
    id: int
    subject: str