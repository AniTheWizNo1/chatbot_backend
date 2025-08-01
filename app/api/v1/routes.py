from fastapi import APIRouter, Depends, Query, HTTPException
from typing import Optional

from app.schemas.predict import PredictRequest
from app.schemas.history import HistoryResponse
from app.services.predictor import get_prediction
from app.services.history import save_message, get_history
from app.core.firebase import verify_firebase_token  # Firebase auth
from app.database.db import db

router = APIRouter()

@router.post("/predict")
async def predict(
    request: PredictRequest, 
    user: dict = Depends(verify_firebase_token)  # Firebase user data
):
    result = get_prediction(request.dict())
    save_message(request.user_id, request.message, result, request.session_id)
    return {"result": result}

@router.get("/history", response_model=HistoryResponse)
async def history(
    user_id: str = Query(...), 
    user: dict = Depends(verify_firebase_token)
):
    return get_history(user_id)

@router.delete("/history")
async def delete_history(
    user_id: str = Query(...),
    session_id: Optional[str] = Query(None),
    user: dict = Depends(verify_firebase_token)
):
    query = {"user_id": user_id}
    if session_id:
        query["session_id"] = session_id

    result = db.chat_history.delete_many(query)
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="No matching records found.")
    return {"deleted_count": result.deleted_count}
