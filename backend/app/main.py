from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.trace_routes import router as trace_router
app = FastAPI()
app.include_router(trace_router)
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AgentScope AI Backend Running"}