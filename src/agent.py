import os
import google.generativeai as genai
from deepeval.tracing import observe

class JiraAgent:
    def __init__(self):
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    @observe(type="tool")
    def create_issue(self, project: str, summary: str, priority: str):
        return {"status": "success", "issue_key": f"{project}-101"}

    @observe()
    def run(self, user_input: str):
        # In a real agent, you'd use Gemini's function calling feature.
        # For this PoC, we are simulating the reasoning process.
        prompt = f"System: Use create_issue tool for Jira requests. User: {user_input}"
        response = self.model.generate_content(prompt)
        
        # Simulate tool execution based on LLM intent
        self.create_issue(project="OPS", summary=user_input, priority="High")
        return response.text