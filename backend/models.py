

from pydantic import BaseModel, Field
from typing import Optional


class ScoreRequest(BaseModel):
    username: str = Field(..., min_length=1, max_length=50)
    topic: str = Field(..., min_length=1, max_length=100)
    score: int = Field(..., ge=0)
    total: int = Field(..., gt=0)


class ScoreResponse(BaseModel):
    message: str
    username: str
    topic: str
    percentage: float


class LoginRequest(BaseModel):
    username: str = Field(..., min_length=1, max_length=50)


class LoginResponse(BaseModel):
    message: str
    username: str


class FeedbackRequest(BaseModel):
    username: str = Field(..., min_length=1, max_length=50)
    message: str = Field(..., min_length=1, max_length=500)
    rating: Optional[int] = Field(default=None, ge=1, le=5)