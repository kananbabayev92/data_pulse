from pydantic import BaseModel
from typing import Optional


class PostBase(BaseModel):
    title: str
    body: Optional[str]


class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int

    class config():
        orm_mode = True

