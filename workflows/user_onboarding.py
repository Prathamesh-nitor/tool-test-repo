from langgraph.graph import StateGraph, END
from langchain.prompts import PromptTemplate
from chains.send_email import send_welcome_email
from chains.log_activity import log_activity
from services.user_service import create_user
from utils.pii import filter_pii
def user_onboarding_workflow(input_data: dict, current_user):
    state = {}
    # Step 1: Validate input data
    filtered_input = filter_pii(input_data)
    if not filtered_input.get("name") or not filtered_input.get("email") or not filtered_input.get("password"):
        return {"error": "Invalid input"}
    # Step 2: Create User
    user = create_user(filtered_input)
    # Step 3: Send Welcome Email
    send_welcome_email(user.email, user.name)
    # Step 4: Log Activity
    log_activity(current_user.email, "User Onboarding", {"user_id": user.id})
    return {"id": user.id, "message": "User created successfully"}