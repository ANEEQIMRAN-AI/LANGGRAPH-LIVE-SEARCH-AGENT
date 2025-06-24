# prompts.py
from langchain.prompts import PromptTemplate

search_summary_prompt = PromptTemplate.from_template("""
You are an expert research assistant with access to recent internet data.

Using the search results below, provide a complete, accurate, and concise answer to the user question.

User Question:
"{query}"

Search Results:

{context}


Instructions:
- Write in clear, natural language.
- Only include information that appears in the search results.
- Do not hallucinate or add unsupported facts.
- If data is conflicting or missing, mention that clearly.

Return only the final answer.
""")
