from fastapi import FastAPI
from api.user import router as user_router
from api.workflow import router as workflow_router
from api.auth import router as auth_router
from core.config import setup_logging
from starlette.middleware.base import BaseHTTPMiddleware
from core.security import CustomHeaderMiddleware
setup_logging()
app = FastAPI(title="User Workflow API", version="1.0.0")
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(workflow_router, prefix="/workflows", tags=["workflows"])
app.add_middleware(CustomHeaderMiddleware)