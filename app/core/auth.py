from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.config import SECRET_KEY

security = HTTPBearer()

def token_required(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    print(f"🟢 Received token only: {token}")
    print(f"🔐 Expected token: {SECRET_KEY}")
    if token != SECRET_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    return True
