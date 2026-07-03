from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from core.config import SECRET_KEY, ALGORITHM
from models.user import UserOut
from services.user_service import get_user_by_email
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")
class CustomHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers['X-Custom-Header'] = 'Hello from middleware!'
        return response
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user_by_email(email)
    if user is None:
        raise credentials_exception
    return user
def require_role(role: str):
    def dependency(current_user: UserOut = Depends(get_current_user)):
        if role not in current_user.roles:
            raise HTTPException(status_code=403, detail="Not enough privileges")
        return current_user
    return dependency