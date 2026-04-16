from app.agents.base_agent import BaseAgent
from app.services.llm_service import call_llm


class FeedbackAgent(BaseAgent):

    def run(self, input_data):
        question = input_data["question"]
        answer = input_data["answer"]
        evaluation = input_data["evaluation"]

        prompt = f"""
You are an expert interview coach.

Based on the evaluation, give actionable feedback.

Question:
{question}

Answer:
{answer}

Evaluation:
Score: {evaluation['score']}
Feedback: {evaluation['feedback']}
Weak Area: {evaluation['weak_area']}

Give:
- 2-3 bullet points
- How to improve
- Be specific and practical
- Keep it short
"""

        feedback = call_llm(prompt)

        return {
            "detailed_feedback": feedback.strip()
        }