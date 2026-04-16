from typing import Dict, List, Optional

class MemoryStore:
    def __init__(self):
        self.sessions: Dict[str, List[dict]] = {}

    def create_session(self, session_id: str):
        if session_id not in self.sessions:
            self.sessions[session_id] = []

    def add_interaction(self, session_id: str, data: dict):
        """
        Expected data format:
        {
            "question": str,
            "answer": Optional[str],
            "evaluation": Optional[dict]
        }
        """
        self.sessions[session_id].append(data)

    def get_history(self, session_id: str):
        return self.sessions.get(session_id, [])