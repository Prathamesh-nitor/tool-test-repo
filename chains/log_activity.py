from core.audit import log_action
def log_activity(user_email: str, action: str, details: dict):
    log_action(user_email, action, details)