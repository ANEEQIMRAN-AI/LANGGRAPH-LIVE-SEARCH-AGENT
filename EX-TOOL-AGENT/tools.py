# tools.py
import os
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()

# Initialize Tavily Search Tool
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY not found in environment variables.")

search_tool = TavilySearchResults(api_key=TAVILY_API_KEY)

def perform_search(query: str) -> str:
    """
    Performs a live web search using Tavily and returns summarized text.
    """
    results = search_tool.run(query)
    return "\n\n".join([r["content"] for r in results])
