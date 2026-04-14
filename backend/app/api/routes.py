from fastapi import APIRouter
from app.models.schemas import InterviewRequest
from app.agents.question_agent import QuestionAgent

router = APIRouter()

@router.post("/start-interview")
def start_interview(request: InterviewRequest):
    agent = QuestionAgent()
    result = agent.run(request.dict())
    return result