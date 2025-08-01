from pydantic import BaseModel
from typing import Optional

class PredictRequest(BaseModel):
    user_id: str
    message: str
    session_id: Optional[str] = None  # ⬅️ Optional field
