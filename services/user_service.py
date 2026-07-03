from models.user import UserCreate, UserOut, UserInDB
from passlib.context import CryptContext
from typing import Optional
from jose import jwt
from core.config import SECRET_KEY, ALGORITHM
from utils.pii import filter_pii
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
_fake_db = {}
_id_counter = 1
def get_user_by_email(email: str) -> Optional[UserOut]:
    for user in _fake_db.values():
        if user.email == email:
            return user
    return None
def create_user(user: UserCreate) -> UserOut:
    global _id_counter
    hashed_password = pwd_context.hash(user.password)
    user_out = UserOut(id=_id_counter, name=user.name, email=user.email, roles=["user"])
    _fake_db[_id_counter] = UserInDB(**user_out.dict(), hashed_password=hashed_password)
    _id_counter += 1
    return user_out
def get_user(user_id: int) -> Optional[UserOut]:
    user = _fake_db.get(user_id)
    if user:
        return UserOut(**user.dict())
    return None
def delete_user(user_id: int) -> bool:
    if user_id in _fake_db:
        del _fake_db[user_id]
        return True
    return False
def authenticate_user(email: str, password: str) -> Optional[UserOut]:
    for user in _fake_db.values():
        if user.email == email and pwd_context.verify(password, user.hashed_password):
            return UserOut(**user.dict())
    return None
def create_access_token(data: dict):
    from datetime import datetime, timedelta
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt