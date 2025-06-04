from langgraph.graph import StateGraph, END, START
from app.agents.core.state import ChatbotState
from langgraph.checkpoint.memory import MemorySaver
from app.agents.core.nodes import AgentNodes
from app.agents.core.router import RouterNode


def build_graph() -> StateGraph:
    builder = StateGraph(ChatbotState)
    node = AgentNodes()
    router = RouterNode()
    
    # Nodes
    builder.add_node("greeting_node", node.greeting_node)
    builder.add_node("get_user_problem_node", node.get_user_problem_node)
    builder.add_node("get_problem_node", node.get_problem_node)
    builder.add_node("followup_problem_detect_node", node.followup_problem_detect_node)
    builder.add_node("emotion_support_node", node.emotion_support_node)
    builder.add_node("get_user_emotion_node", node.get_user_emotion_node)
    builder.add_node("problem_depth_analysis_node", node.problem_depth_analysis_node)
    builder.add_node("ask_emotion_check_node", node.ask_emotion_check_node)
    builder.add_node("ask_other_node", node.ask_other_node)
    builder.add_node("ask_phq_9_node", node.ask_phq_9_node)
    builder.add_node("get_user_answer_phq9_node", node.get_user_answer_phq9_node)
    builder.add_node("get_level_of_depression_node", node.get_level_of_depression_node)
    builder.add_node("problem_summary_node", node.problem_summary_node)
    
    # Routers
    builder.add_node("check_problem_detected_router", router.check_problem_detected_router)
    builder.add_node("check_problem_depth_analysis_router", router.check_problem_depth_analysis_router)
    builder.add_node("check_full_phq9_answer_router", router.check_full_phq9_answer_router)
    
    builder.add_edge(START, "greeting_node")
    builder.add_edge("greeting_node", "get_user_problem_node")
    builder.add_edge("get_user_problem_node", "get_problem_node")
    builder.add_edge("get_problem_node", "check_problem_detected_router")
    builder.add_conditional_edges(
        "check_problem_detected_router",
        lambda state: state["next_node"],
        {
            "detected": "emotion_support_node",
            "insufficient_info": "followup_problem_detect_node"
        }
    )
    
    builder.add_edge("followup_problem_detect_node", "get_user_problem_node")
    builder.add_edge("emotion_support_node", "get_user_emotion_node")
    builder.add_edge("get_user_emotion_node", "problem_depth_analysis_node")
    builder.add_edge("problem_depth_analysis_node", "check_problem_depth_analysis_router")
    
    builder.add_conditional_edges(
        "check_problem_depth_analysis_router",
        lambda state: state["next_node"],
        {
            "move_to_step_5": "problem_summary_node",
            "ask_PHQ9": "ask_phq_9_node",
            "ask_other": "ask_other_node",
            "ask_emotion_check": "ask_emotion_check_node",
        }
    )
    
    builder.add_edge("ask_emotion_check_node", "get_user_emotion_node")
    builder.add_edge("ask_other_node", "get_user_emotion_node")
    
    builder.add_edge("ask_phq_9_node", "get_user_answer_phq9_node")
    builder.add_edge("get_user_answer_phq9_node", "check_full_phq9_answer_router")
    builder.add_conditional_edges(
        "check_full_phq9_answer_router",
        lambda state: state["next_node"],
        { 
            "yes": "get_level_of_depression_node",
            "no": "ask_phq_9_node"
        }
    )
    builder.add_edge("get_level_of_depression_node", "problem_summary_node")
    
    builder.add_edge("problem_summary_node", END)
    
    
    memory = MemorySaver()
    
    graph = builder.compile(checkpointer=memory)
    
    return graph