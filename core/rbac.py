from fastapi import Depends, HTTPException
from core.security import get_current_user
def require_role(role: str):
    def dependency(current_user=Depends(get_current_user)):
        if role not in getattr(current_user, "roles", []):
            raise HTTPException(status_code=403, detail="Not enough privileges")
        return current_user
    return dependency