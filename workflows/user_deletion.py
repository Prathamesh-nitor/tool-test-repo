from langgraph.graph import StateGraph, END
from chains.log_activity import log_activity
from services.user_service import get_user, delete_user
def user_deletion_workflow(input_data: dict, current_user):
    user_id = input_data.get("id")
    # Step 1: Validate user existence
    user = get_user(user_id)
    if not user:
        return {"error": "User not found"}
    # Step 2: Delete User
    deleted = delete_user(user_id)
    if not deleted:
        return {"error": "User not found"}
    # Step 3: Log Deletion
    log_activity(current_user.email, "User Deletion", {"user_id": user_id})
    return {"message": "User deleted successfully"}