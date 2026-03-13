import os
import google.generativeai as genai
from deepeval.tracing import observe

class JiraAgent:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY", "").strip().replace('"', '').replace("'", "")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash") # Use 1.5 Flash

    @observe(type="tool")
    def create_issue(self, project: str, summary: str, priority: str):
        return {"status": "success", "issue_key": f"{project}-101"}

    @observe()
    def run(self, user_input: str):
        prompt = f"System: Use create_issue tool. User: {user_input}"
        # Standard generate call
        response = self.model.generate_content(prompt)
        
        # Simulating logic
        self.create_issue(project="OPS", summary=user_input, priority="High")
        return response.text