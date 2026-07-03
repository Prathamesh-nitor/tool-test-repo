from fastapi import APIRouter, Depends, HTTPException
from models.workflow import WorkflowRequest, WorkflowResponse
from core.security import require_role, get_current_user
from workflows.user_onboarding import user_onboarding_workflow
from workflows.user_deletion import user_deletion_workflow
router = APIRouter()
@router.post("/onboarding", response_model=WorkflowResponse)
def run_user_onboarding(request: WorkflowRequest, current_user=Depends(require_role("admin"))):
    result = user_onboarding_workflow(request.input_data, current_user)
    return WorkflowResponse(result=result)
@router.post("/deletion", response_model=WorkflowResponse)
def run_user_deletion(request: WorkflowRequest, current_user=Depends(require_role("admin"))):
    result = user_deletion_workflow(request.input_data, current_user)
    return WorkflowResponse(result=result)