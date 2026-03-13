import pytest
# 1. ADD THESE IMPORTS (This fixes ToolCall, LLMTestCase, and assert_test)
from deepeval import assert_test
from deepeval.test_case import LLMTestCase, ToolCall
from deepeval.metrics import ToolCorrectnessMetric

# 2. IMPORT YOUR AGENT AND GEMINI MODEL
from src.agent import JiraAgent
from src.gemini_model import Gemini2Flash 

def test_jira_logic():
    # 3. INITIALIZE THE CLASSES
    gemini_judge = Gemini2Flash()
    agent = JiraAgent() # This defines 'agent' so line 19 works
    
    user_prompt = "Create a high priority bug for the login crash in project OPS"
    
    # 4. RUN THE AGENT
    actual_output = agent.run(user_prompt)
    
    # 5. DEFINE EXPECTATIONS
    expected_tools = [ToolCall(name="create_issue")]

    test_case = LLMTestCase(
        input=user_prompt,
        actual_output=actual_output,
        expected_tools=expected_tools
    )

    # 6. DEFINE METRIC
    metric = ToolCorrectnessMetric(threshold=0.8, model=gemini_judge)
    
    # 7. RUN TEST
    assert_test(test_case, [metric])