from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv(override=True)

class TherapyChain():
    def __init__(self):
        self.model_name = os.getenv('MODEL_NAME')
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.llm = ChatGoogleGenerativeAI(
            model=self.model_name,
            api_key=self.api_key
        )
    
    def greeting(self) -> LLMChain:
        with open("app/agents/chain/prompts/greeting_prompt.txt", encoding="utf-8") as f:
            prompt_text = f.read()
        
        prompt = PromptTemplate.from_template(prompt_text)
        chain = prompt | self.llm
        return chain
    
    def proplem_detect(self) -> LLMChain:
        with open("app/agents/chain/prompts/proplem_detect_prompt.txt", encoding="utf-8") as f:
            prompt_text = f.read()
        
        prompt = PromptTemplate.from_template(prompt_text)
        chain = prompt | self.llm
        return chain
    
    def followup_problem_detect(self) -> LLMChain:
        with open("app/agents/chain/prompts/followup_problem_detect_prompt.txt", encoding="utf-8") as f:
            prompt_text = f.read()
        
        prompt = PromptTemplate.from_template(prompt_text)
        chain = prompt | self.llm
        return chain
    
    def emotion_support(self) -> LLMChain:
        with open("app/agents/chain/prompts/emotion_support_prompt.txt", encoding="utf-8") as f:
            prompt_text = f.read()
        
        prompt = PromptTemplate.from_template(prompt_text)
        chain = prompt | self.llm
        return chain
    
    def problem_depth_analysis(self) -> LLMChain:
        with open("app/agents/chain/prompts/problem_depth_analysis_prompt.txt", encoding="utf-8") as f:
            prompt_text = f.read()
        
        prompt = PromptTemplate.from_template(prompt_text)
        chain = prompt | self.llm
        return chain
    
    def ask_emotion_check(self) -> LLMChain:
        with open("app/agents/chain/prompts/ask_emotion_check_prompt.txt", encoding="utf-8") as f:
            prompt_text = f.read()
        
        prompt = PromptTemplate.from_template(prompt_text)
        chain = prompt | self.llm
        return chain

    def ask_PHQ9(self) -> LLMChain:
        with open("app/agents/chain/prompts/ask_PHQ9_prompt.txt", encoding="utf-8") as f:
            prompt_text = f.read()
        
        prompt = PromptTemplate.from_template(prompt_text)
        chain = prompt | self.llm
        return chain
    
    def analyze_PHQ9(self) -> LLMChain:
        with open("app/agents/chain/prompts/analyze_PHQ9_prompt.txt", encoding="utf-8") as f:
            prompt_text = f.read()
        
        prompt = PromptTemplate.from_template(prompt_text)
        chain = prompt | self.llm
        return chain
    
    def ask_other(self) -> LLMChain:
        with open("app/agents/chain/prompts/ask_other_prompt.txt", encoding="utf-8") as f:
            prompt_text = f.read()
        
        prompt = PromptTemplate.from_template(prompt_text)
        chain = prompt | self.llm
        return chain
    
    def move_to_step_5(self) -> LLMChain:
        with open("app/agents/chain/prompts/move_to_step_5_prompt.txt", encoding="utf-8") as f:
            prompt_text = f.read()
        
        prompt = PromptTemplate.from_template(prompt_text)
        chain = prompt | self.llm
        return chain
    
    def problem_summary(self) -> LLMChain:
        with open("app/agents/chain/prompts/problem_summary_prompt.txt", encoding="utf-8") as f:
            prompt_text = f.read()
        
        prompt = PromptTemplate.from_template(prompt_text)
        chain = prompt | self.llm
        return chain