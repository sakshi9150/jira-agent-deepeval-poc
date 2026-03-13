import os
import google.generativeai as genai
from deepeval.tracing import observe

class JiraAgent:
    def __init__(self):
        # 1. Get and clean the API key (fixes 'Illegal Header' errors)
        api_key = os.getenv("GOOGLE_API_KEY", "").strip().replace('"', '').replace("'", "")
        
        if not api_key:
            raise ValueError("GOOGLE_API_KEY is missing in agent.py!")

        genai.configure(api_key=api_key)
        
        # 2. Use 1.5-flash for better stability on the Free Tier
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    @observe(type="tool")
    def create_issue(self, project: str, summary: str, priority: str):
        return {"status": "success", "issue_key": f"{project}-101"}

    @observe()
    def run(self, user_input: str):
        # The prompt tells the LLM what to do
        prompt = f"System: You are a Jira assistant. Use the create_issue tool for Jira requests. User: {user_input}"
        
        # 3. LLM Reasoning
        response = self.model.generate_content(prompt)
        
        # 4. Simulate the tool execution
        self.create_issue(project="OPS", summary=user_input, priority="High")
        
        return response.text