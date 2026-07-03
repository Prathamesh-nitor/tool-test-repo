from pydantic import BaseModel
from datetime import datetime
class AuditLog(BaseModel):
    id: int
    action: str
    timestamp: datetime
    user_email: str
    details: dict