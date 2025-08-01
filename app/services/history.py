from app.database.db import db
from datetime import datetime

def save_message(user_id: str, message: str, response: str, session_id: str = None):
    chat_log = {
        "user_id": user_id,
        "session_id": session_id,
        "message": message,
        "response": response,
        "created_at": datetime.utcnow()  # UTC timestamp
    }
    db.chat_history.insert_one(chat_log)
def get_history(user_id: str):
    records = db.chat_history.find({"user_id": user_id}).sort("created_at", 1)
    history = [
        {
            "message": r["message"],
            "response": r["response"],
            "created_at": r.get("created_at")
        }
        for r in records
    ]
    return {"user_id": user_id, "history": history}

