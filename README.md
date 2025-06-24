# LangGraph-WebSearch-Agent

**LangGraph-WebSearch-Agent** is an intelligent, real-time research assistant that leverages **LangGraph**, **LangChain**, **Tavily**, and **Gemini LLM** to search the internet and provide accurate, human-quality answers through a clean **Streamlit interface**.

---

## 🔍 Key Features

✅ Real-time web search powered by [Tavily](https://tavily.com/)  
✅ High-quality answers generated using Gemini 1.5 Pro LLM  
✅ Modular pipeline built with LangGraph & LangChain  
✅ Clean and interactive web interface using Streamlit  
✅ Ideal for current affairs, research, and daily queries

---

## 🧠 Workflow Pipeline

```text
User Question → Tavily Search Tool → Gemini LLM → Final Answer
```

- **Search Tool**: Queries the latest information using Tavily
- **LLM Agent**: Summarizes results with accurate, coherent natural language
- **LangGraph**: Controls flow between agents and tools
- **Streamlit**: Offers a smooth, responsive front-end

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/LangGraph-WebSearch-Agent.git
cd LangGraph-WebSearch-Agent
```

### 2. Set Up Environment
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Add API Keys
Create a `.env` file:
```env
GOOGLE_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 4. Run the App
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```bash
├── app.py               # Streamlit web interface
├── tools.py             # Tavily web search tool
├── prompts.py           # LLM prompt template
├── graphbuilder.py      # LangGraph orchestration logic
├── .env.template        # Environment variable example
├── requirements.txt     # Dependencies
```

---

## 🔧 Built With
- [LangChain](https://www.langchain.com/)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Tavily API](https://app.tavily.com)
- [Gemini LLM](https://deepmind.google/technologies/gemini)
- [Streamlit](https://streamlit.io)

---

## 🛡 License
MIT License © 2025 Aneeq Imran

---

## 🤝 Contributing
Contributions and feedback are welcome! Please fork the repo, create a pull request, or open an issue for suggestions.

---

## 📬 Contact
**Author**: Aneeq Imran  
**Email**: aneeqimran.ai@gmail.com  
**LinkedIn**: [ANEEQ IMRAN](https://www.linkedin.com/in/aneeq-imran-977077340/)
