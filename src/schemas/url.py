from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class URLCreate(BaseModel):
  original_url: str
  expires_at: Optional[datetime] = None


class URLResponse(BaseModel):
  id: int
  original_url: str
  short_code: str
  is_active: bool
  expires_at: Optional[datetime] = None