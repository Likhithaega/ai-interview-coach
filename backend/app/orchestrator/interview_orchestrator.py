import uuid
from app.memory.memory_store import MemoryStore
from app.agents.question_agent import QuestionAgent
from app.agents.evaluation_agent import EvaluationAgent
from app.agents.feedback_agent import FeedbackAgent

memory = MemoryStore()


class InterviewOrchestrator:

    def start_interview(self, role, level):
        session_id = str(uuid.uuid4())

        memory.create_session(session_id)

        agent = QuestionAgent()
        result = agent.run({"role": role, "level": level})

        memory.add_interaction(session_id, {
            "question": result["question"],
            "answer": None,
            "evaluation": None,
            "feedback": None
        })

        return {
            "session_id": session_id,
            "question": result["question"]
        }

    def next_question(self, session_id, answer):
        history = memory.get_history(session_id)

        # 1. Get last interaction
        last_interaction = history[-1]

        # 2. Save answer
        last_interaction["answer"] = answer

        # 3. Evaluate answer
        evaluator = EvaluationAgent()
        evaluation = evaluator.run({
            "question": last_interaction["question"],
            "answer": answer
        })

        # 4. Store evaluation
        last_interaction["evaluation"] = evaluation

        # 5. Generate detailed feedback
        feedback_agent = FeedbackAgent()
        feedback = feedback_agent.run({
            "question": last_interaction["question"],
            "answer": answer,
            "evaluation": evaluation
        })

        # 6. Store feedback
        last_interaction["feedback"] = feedback

        # 7. Build context from full history
        context = ""
        for item in history:
            context += f"""
Question: {item['question']}
Answer: {item['answer']}
Evaluation: {item.get('evaluation')}
Feedback: {item.get('feedback')}
"""

        # 8. Generate next question
        agent = QuestionAgent()
        result = agent.run({
            "role": "python developer",
            "level": "beginner",
            "context": context
        })

        # 9. Save new question
        memory.add_interaction(session_id, {
            "question": result["question"],
            "answer": None,
            "evaluation": None,
            "feedback": None
        })

        # 10. Return full response
        return {
            "evaluation": evaluation,
            "feedback": feedback,
            "next_question": result["question"]
        }