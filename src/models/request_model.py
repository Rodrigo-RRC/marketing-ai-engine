"""
Pydantic model for validating user request.
"""

from pydantic import BaseModel, Field


class ContentRequest(BaseModel):
    topic: str = Field(min_length=3)
    platform: str
    tone: str
    audience: str
    length: str
    include_cta: bool
    include_hashtags: bool
    include_emojis: bool
    keywords: str | None = None