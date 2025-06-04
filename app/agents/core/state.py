from typing import TypedDict, List, Dict, Any, Annotated
from langgraph.graph.message import add_messages

def get_phq_9_question() -> List[dict]:
    return [
        {
            "index": 1,
            "question": "Trong 2 tuần qua, bạn có cảm thấy ít hứng thú hoặc không còn thấy thích thú khi làm việc gì đó không?",
            "answer_text": None
        },
        {
            "index": 2,
            "question": "Trong 2 tuần qua, bạn có cảm thấy buồn, chán nản hoặc tuyệt vọng không?",
            "answer_text": None
        },
        {
            "index": 3,
            "question": "Trong 2 tuần qua, bạn có gặp khó khăn khi ngủ hoặc ngủ quá nhiều không?",
            "answer_text": None
        },
        {
            "index": 4,
            "question": "Trong 2 tuần qua, bạn có cảm thấy mệt mỏi hoặc thiếu năng lượng không?",
            "answer_text": None
        },
        {
            "index": 5,
            "question": "Trong 2 tuần qua, bạn có cảm thấy chán ăn hoặc ăn quá nhiều không?",
            "answer_text": None
        },
        {
            "index": 6,
            "question": "Trong 2 tuần qua, bạn có cảm thấy mình là người thất bại hoặc khiến bản thân hoặc gia đình thất vọng không?",
            "answer_text": None
        },
        {
            "index": 7,
            "question": "Trong 2 tuần qua, bạn có gặp khó khăn trong việc tập trung vào những việc như đọc sách hay xem TV không?",
            "answer_text": None
        },
        {
            "index": 8,
            "question": "Trong 2 tuần qua, bạn có di chuyển hoặc nói chậm hơn bình thường đến mức người khác có thể nhận thấy không? Hoặc ngược lại – cảm thấy bồn chồn hoặc không thể ngồi yên?",
            "answer_text": None
        },
        {
            "index": 9,
            "question": "Trong 2 tuần qua, bạn có nghĩ rằng thà chết còn hơn sống hoặc nghĩ đến việc tự làm hại bản thân không?",
            "answer_text": None
        }
    ]


class ChatbotState(TypedDict):
    user_input: str
    user_id: int
    messages: Annotated[list, add_messages]
    next_node: str
    nodes_flow: List[str]
    last_question: str
    
    problem_detection: dict
    problem_depth_analysis: dict
    problem_analysis_start_index: int
    
    phq9_progress: List[dict]
    phq9_index: int
    stress_level: str
    
    problem_summary: str
    
def init_chatbot_state() -> ChatbotState:
    return ChatbotState(
        user_input="",
        user_id=None,
        messages=[],  # dùng Annotated[list, add_messages]
        next_node=None,
        nodes_flow=[],
        last_question=None,
        
        problem_detection=None,
        problem_depth_analysis=None,
        problem_analysis_start_index=None,
        
        phq9_progress=get_phq_9_question(),
        phq9_index=None,
        stress_level=None,

        problem_summary=None
    )