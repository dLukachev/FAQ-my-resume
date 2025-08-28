from fastapi import APIRouter
from pydantic import BaseModel
from src.core.service_rag import generate_answer

router = APIRouter()

class QuestRequest(BaseModel):
    quest: str
    chat_id: str = "default"

@router.post("/api/get_data")
def api_get_data(request: QuestRequest):
    answer, debug = generate_answer(request.quest, request.chat_id)
    return {"success": answer, "debug": debug}