# app.py
import streamlit as st
from graphbuilder import build_websearch_graph

st.set_page_config(page_title="WebSearch Agent", page_icon="🔍")
st.title("🔍 Web Search Agent with LangGraph")

user_query = st.text_input("Enter your question:", placeholder="e.g., What are the latest AI trends in 2025?")

if user_query:
    st.info("Running search and generating answer using Gemini LLM...", icon="⚙️")
    app = build_websearch_graph()
    result = app.invoke({"query": user_query})
    
    st.markdown("---")
    st.subheader("📄 Answer")
    st.write(result['final_answer'])
