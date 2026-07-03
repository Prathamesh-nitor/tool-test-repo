from pydantic import BaseModel
from typing import Any, Dict
class WorkflowRequest(BaseModel):
    input_data: Dict[str, Any]
class WorkflowResponse(BaseModel):
    result: Dict[str, Any]