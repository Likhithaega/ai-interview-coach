from app.agents.base_agent import BaseAgent
from app.services.llm_service import call_llm
import json
import re


class EvaluationAgent(BaseAgent):

    def extract_json(self, text: str):
        """
        Extract JSON block from LLM response safely
        """
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return match.group()
        raise ValueError("No valid JSON found in response")

    def run(self, input_data):
        question = input_data["question"]
        answer = input_data["answer"]

        prompt = f"""
You are an expert technical interviewer.

Evaluate the candidate's answer.

Question:
{question}

Answer:
{answer}

STRICT RULES:
- Return ONLY JSON
- No explanation
- No extra text

Format:
{{
  "score": 0-10,
  "feedback": "short feedback",
  "weak_area": "topic name"
}}
"""

        result = call_llm(prompt).strip()

        print("LLM RAW:", result)  # Debug log

        try:
            json_str = self.extract_json(result)
            return json.loads(json_str)

        except Exception as e:
            print("JSON Parsing Error:", e)

            # Fallback (VERY IMPORTANT)
            return {
                "score": 5,
                "feedback": "Could not evaluate answer properly",
                "weak_area": "unknown"
            }