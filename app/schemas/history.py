from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Message(BaseModel):
    message: str
    response: str
    created_at: Optional[datetime]  # new field

class HistoryResponse(BaseModel):
    user_id: str
    history: List[Message]
