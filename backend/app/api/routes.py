from fastapi import APIRouter
from app.models.schemas import InterviewRequest
from app.orchestrator.interview_orchestrator import InterviewOrchestrator

router = APIRouter()
orchestrator = InterviewOrchestrator()

@router.post("/start-interview")
def start_interview(request: InterviewRequest):
    return orchestrator.start_interview(request.role, request.level)


@router.post("/next-question")
def next_question(session_id: str, answer: str):
    return orchestrator.next_question(session_id, answer)