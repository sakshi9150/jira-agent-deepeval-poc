import os
import google.generativeai as genai
from deepeval.models.base_model import DeepEvalBaseLLM

# Make sure this name is EXACTLY Gemini2Flash
class Gemini2Flash(DeepEvalBaseLLM):
    def __init__(self, model_name="gemini-1.5-flash"):
        self.model_name = model_name
        api_key = os.getenv("GOOGLE_API_KEY", "").strip().replace('"', '').replace("'", "")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def load_model(self):
        return self.model

    def generate(self, prompt: str) -> str:
        res = self.model.generate_content(prompt)
        return res.text

    async def a_generate(self, prompt: str) -> str:
        res = await self.model.generate_content_async(prompt)
        return res.text

    def get_model_name(self):
        return self.model_name