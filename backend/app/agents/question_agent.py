from app.agents.base_agent import BaseAgent
from app.services.llm_service import call_llm

class QuestionAgent(BaseAgent):

    def run(self, input_data):
        role = input_data.get("role", "software engineer")
        level = input_data.get("level", "beginner")
        context = input_data.get("context", "")

        prompt = f"""
        You are a technical interviewer.

        Previous conversation:
        {context}

        Generate ONLY ONE interview question.

        STRICT RULES:
        - Output ONLY the question
        - No explanations
        - No hints
        - No extra text
        - Keep it under 2 lines
        - Make it relevant to a {level} {role}

        Question:
        """
        question = call_llm(prompt)

        return {"question": question}