from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes_rag import router as rag_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rag_router)