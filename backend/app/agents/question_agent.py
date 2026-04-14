from app.agents.base_agent import BaseAgent
from app.services.llm_service import call_llm

class QuestionAgent(BaseAgent):

    def run(self, input_data):
        role = input_data.get("role", "software engineer")
        level = input_data.get("level", "beginner")

        prompt = f"""
        You are an expert technical interviewer.

        Generate ONE interview question for a {level} {role}.

        Rules:
        - Be clear and concise
        - Do NOT give answer
        """

        question = call_llm(prompt)

        return {
            "question": question
        }