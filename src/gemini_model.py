import os
import google.generativeai as genai
from deepeval.models.base_model import DeepEvalBaseLLM

class Gemini2Flash(DeepEvalBaseLLM):
    def __init__(self, model_name="gemini-2.0-flash"):
        self.model_name = model_name
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel(model_name)

    def load_model(self):
        return self.model

    def generate(self, prompt: str) -> str:
        chat_model = self.load_model()
        res = chat_model.generate_content(prompt)
        return res.text

    async def a_generate(self, prompt: str) -> str:
        chat_model = self.load_model()
        res = await chat_model.generate_content_async(prompt)
        return res.text

    def get_model_name(self):
        return self.model_name