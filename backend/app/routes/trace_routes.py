from fastapi import APIRouter
from app.models.trace_model import Trace
from app.services.trace_service import add_trace, get_traces

router = APIRouter()

@router.post("/trace")
def create_trace(trace: Trace):
    add_trace(trace)
    return {
        "message": "Trace added successfully"
    }

@router.get("/traces")
def fetch_traces():
    return get_traces()