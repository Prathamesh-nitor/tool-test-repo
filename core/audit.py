from datetime import datetime
from loguru import logger
def log_action(user_email: str, action: str, details: dict):
    logger.info(f"{datetime.utcnow().isoformat()} | {user_email} | {action} | {details}")