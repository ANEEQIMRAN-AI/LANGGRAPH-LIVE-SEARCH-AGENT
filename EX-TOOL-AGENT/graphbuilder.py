# graphbuilder.py
from langchain_core.runnables import RunnableLambda
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from prompt import search_summary_prompt
from tools import perform_search
import os
from dotenv import load_dotenv

load_dotenv()

# LLM setup
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

# Define state type
AgentState = dict[str, str]

# Step 1: Search Node
def run_search(state: AgentState) -> AgentState:
    query = state["query"]
    results = perform_search(query)
    return {"query": query, "context": results}

# Step 2: LLM Answering Node
def generate_answer(state: AgentState) -> AgentState:
    prompt = search_summary_prompt.format(query=state["query"], context=state["context"])
    response = llm.invoke(prompt)
    return {"final_answer": response.content}

# Build LangGraph

def build_websearch_graph():
    graph = StateGraph(state_schema=AgentState)
    graph.add_node("search", RunnableLambda(run_search))
    graph.add_node("llm", RunnableLambda(generate_answer))

    graph.set_entry_point("search")
    graph.add_edge("search", "llm")
    graph.add_edge("llm", END)

    return graph.compile()
