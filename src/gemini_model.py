import os
import google.generativeai as genai
from deepeval.models.base_model import DeepEvalBaseLLM

class Gemini2Flash(DeepEvalBaseLLM):
    def __init__(self, model_name="gemini-2.0-flash"):
        self.model_name = model_name
        # This tells the code to find the key in GitHub's hidden settings
        api_key = os.getenv("GOOGLE_API_KEY")
        
        if not api_key:
            raise ValueError("GOOGLE_API_KEY is missing!")

        # This cleanup helps avoid the 'Illegal Header' error
        clean_key = api_key.strip().replace('"', '').replace("'", "")
        genai.configure(api_key=clean_key)
        self.model = genai.GenerativeModel(model_name)

    def generate(self, prompt: str) -> str:
        res = self.model.generate_content(prompt)
        return res.text

    async def a_generate(self, prompt: str) -> str:
        res = await self.model.generate_content_async(prompt)
        return res.text

    def load_model(self): return self.model
    def get_model_name(self): return self.model_name