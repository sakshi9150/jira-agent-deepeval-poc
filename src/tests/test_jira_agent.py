import pytest
from deepeval import assert_test
from deepeval.test_case import LLMTestCase, ToolCall
from deepeval.metrics import ToolCorrectnessMetric

# Fix the import here
from src.agent import JiraAgent
from src.gemini_model import Gemini2Flash 

def test_jira_logic():
    gemini_judge = Gemini2Flash()
    agent = JiraAgent()
    
    user_prompt = "Create a high priority bug for the login crash in project OPS"
    actual_output = agent.run(user_prompt)
    
    expected_tools = [ToolCall(name="create_issue")]

    test_case = LLMTestCase(
        input=user_prompt,
        actual_output=actual_output,
        expected_tools=expected_tools
    )

    metric = ToolCorrectnessMetric(threshold=0.8, model=gemini_judge)
    assert_test(test_case, [metric])