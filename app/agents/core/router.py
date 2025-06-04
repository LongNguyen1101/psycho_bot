from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph.message import add_messages
from langchain.prompts import PromptTemplate
from langgraph.types import interrupt
from app.agents.core.state import ChatbotState
from app.agents.chain.therapy_chain import TherapyChain

import os
from dotenv import load_dotenv
import json

load_dotenv(override=True)

MODEL_NAME = os.getenv("MODEL_NAME")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
CHATBOT_NAME = os.getenv("CHATBOT_NAME")

class RouterNode:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=MODEL_NAME,
            google_api_key=GOOGLE_API_KEY
        )
        self.chain = TherapyChain()
        
    def check_problem_detected_router(self, state: ChatbotState) -> ChatbotState:
        print(f"> Node: check_problem_detected_router")
        
        # next_node_list = ["detected", "insufficient_info"]
        problem_detection = state["problem_detection"]
        status = problem_detection.get("status", "insufficient_info")
        next_node = "insufficient_info"
        
        if status in "detected":
            next_node = status
            print(f"> Problem found: {problem_detection}")
        else:
            next_node = status
            print(f"> Problem not found: {problem_detection}")
        
        state["nodes_flow"].append("check_problem_detected_router")
        state["next_node"] = next_node
        return state
    
    def check_problem_depth_analysis_router(self, state: ChatbotState) -> ChatbotState:
        print(f"> Node: check_problem_depth_analysis_router")
        
        next_node_list = ["move_to_step_5", "ask_PHQ9", "ask_other", "ask_emotion_check"]
        reason = state["problem_depth_analysis"].get("reason", None)
        next_step = state["problem_depth_analysis"].get("next_step", None)
        next_node = "ask_emotion_check"
        
        if reason is not None:
            if next_step in next_node_list:
                next_node = next_step
            else:
                print(f"> next_step not found: {next_step}")
        else:
            print(f"> Cannot find reason in problem_depth_analysis")
        
        state["nodes_flow"].append("check_problem_depth_analysis_router")
        state["next_node"] = next_node
        return state
    
    def check_full_phq9_answer_router(self, state: ChatbotState) -> ChatbotState:
        print(f"> Node: get_full_answer_router")
        next_node = "yes"
        
        phq9_progress = state["phq9_progress"]
        # Check if all of answers are collected
        for data in phq9_progress:
            if data["answer_text"] is None:
                next_node = "no"
                
        print(f"> Full phq9 answer or not: {next_node}")
        
        state["nodes_flow"].append("get_full_answer_router")
        state["next_node"] = next_node
        return state
    