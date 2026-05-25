from pydantic import BaseModel
from datetime import datetime

class Trace(BaseModel):
    agent_name: str
    step_name: str
    input_data: str
    output_data: str
    status: str
    latency: float
    timestamp: datetime