# agents.py: Agent definitions and Team Leader for coordination

class EmpatheticAgent:
    def __init__(self, gemini_api):
        self.gemini_api = gemini_api

    def provide_support(self, user_input: str) -> str:
        if not user_input or len(user_input.strip()) < 5:
            raise ValueError("Input must be at least 5 characters long.")
        return self.gemini_api.generate_response(f"Provide empathetic support for: {user_input}")

class RoutinePlannerAgent:
    def suggest_routine(self) -> str:
        return "Daily Routine: 1. Morning meditation (10 mins), 2. Journal your feelings, 3. Take a walk, 4. Call a friend."

class EmotionalMessageAgent:
    def generate_message(self, user_input: str) -> str:
        if not user_input:
            raise ValueError("Input cannot be empty for message generation.")
        return f"Unsent Message: 'I felt so much when you said {user_input}. I wish I could tell you how it hurt, but I’m letting go now.'"

class TeamLeader:
    def __init__(self):
        # Simulated Gemini API (placeholder)
        from app import GeminiAPI
        self.gemini_api = GeminiAPI()
        self.empathetic_agent = EmpatheticAgent(self.gemini_api)
        self.routine_agent = RoutinePlannerAgent()
        self.message_agent = EmotionalMessageAgent()

    def coordinate(self, user_input: str, image: bytes = None) -> dict:
        # Step 1: Analyze image if provided
        image_analysis = None
        if image:
            image_analysis = self.gemini_api.analyze_image(image)

        # Step 2: Gather responses from agents
        empathetic_response = self.empathetic_agent.provide_support(user_input)
        routine = self.routine_agent.suggest_routine()
        emotional_message = self.message_agent.generate_message(user_input)

        # Step 3: Compile summary
        summary = (
            f"Team Leader Summary:\n"
            f"Image Analysis: {image_analysis or 'No image provided'}\n"
            f"Empathetic Support: {empathetic_response}\n"
            f"Daily Routine: {routine}\n"
            f"Emotional Message: {emotional_message}"
        )

        return {
            "image_analysis": image_analysis,
            "empathetic_response": empathetic_response,
            "daily_routine": routine,
            "emotional_message": emotional_message,
            "summary": summary
        }
