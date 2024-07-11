from pydantic import BaseModel
from typing import Optional


class TopicModel(BaseModel):
    title: str
    description: str
    userId: str


class UpdateTopicModel(BaseModel):
    title: Optional[str]
    description: Optional[str]
    userId: Optional[str]
