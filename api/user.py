from fastapi import APIRouter, Depends, HTTPException, status
from models.user import UserCreate, UserOut
from services.user_service import create_user, get_user, delete_user
from core.security import require_role, get_current_user
from core.audit import log_action
router = APIRouter()
@router.post("/", response_model=UserOut, status_code=201)
def api_create_user(user: UserCreate, current_user=Depends(require_role("admin"))):
    created_user = create_user(user)
    log_action(current_user.email, "create_user", {"user_id": created_user.id})
    return created_user
@router.get("/{id}", response_model=UserOut)
def api_get_user(id: int, current_user=Depends(require_role("admin"))):
    user = get_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
@router.delete("/{id}", status_code=200)
def api_delete_user(id: int, current_user=Depends(require_role("admin"))):
    deleted = delete_user(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    log_action(current_user.email, "delete_user", {"user_id": id})
    return {"message": "User deleted successfully"}