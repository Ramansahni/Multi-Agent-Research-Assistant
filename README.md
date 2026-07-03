# 🤖 Multi-Agent Research Assistant

An AI-powered research assistant that uses a **multi-agent architecture** to automate the entire research workflow. The system performs real-time web search, extracts relevant content from webpages, generates a structured research report, and critically evaluates its own output using specialized AI agents.

## 🌐 Live Demo

**Live Application:** https://multi-agent-research-assistant-genai.streamlit.app/

## 📂 GitHub Repository

**Repository:** https://github.com/Ramansahni/Multi-Agent-Research-Assistant

---

# ✨ Features

- 🔍 **Search Agent** performs real-time web search using Tavily Search API.
- 📄 **Reader Agent** scrapes and extracts relevant content from selected webpages.
- 📝 **Writer Agent** generates structured and detailed research reports.
- 🧐 **Critic Agent** evaluates report quality, highlights strengths, identifies weaknesses, and assigns a quality score.
- ⚡ Interactive Streamlit interface for seamless user experience.
- 🌍 Fetches live information instead of relying solely on pretrained LLM knowledge.
- 🔄 Modular multi-agent pipeline built using LangChain.

---

# 🏗️ System Architecture

```
                 User Query
                      │
                      ▼
              Search Agent
                      │
        Tavily Search API Results
                      │
                      ▼
              Reader Agent
                      │
      Webpage Content Extraction
                      │
                      ▼
              Writer Agent
                      │
      Structured Research Report
                      │
                      ▼
              Critic Agent
                      │
          Report Evaluation
                      │
                      ▼
             Streamlit Interface
```

---

# ⚙️ Tech Stack

### AI & LLM

- LangChain
- Mistral AI
- Prompt Engineering

### Search & Data Collection

- Tavily Search API
- BeautifulSoup
- Requests

### Frontend

- Streamlit

### Backend

- Python

### Utilities

- Python Dotenv
- Rich
- Pydantic
- Pandas

---

# 📁 Project Structure

```
Multi-Agent-Research-Assistant/
│
├── app.py                 # Streamlit UI
├── pipeline.py            # Multi-agent workflow
├── agents.py              # Search, Reader, Writer & Critic agents
├── tools.py               # Search & Scraping tools
├── requirements.txt
├── .env.example
├── LICENSE
└── README.md
```

---

# 🚀 Workflow

1. User enters a research topic.
2. Search Agent retrieves recent information using Tavily Search.
3. Reader Agent extracts detailed content from selected webpages.
4. Writer Agent synthesizes the collected information into a comprehensive research report.
5. Critic Agent reviews the report, provides feedback, and assigns a quality score.
6. Results are displayed through the Streamlit interface.

---

# 💻 Installation

## Clone the repository

```bash
git clone https://github.com/Ramansahni/Multi-Agent-Research-Assistant.git
cd Multi-Agent-Research-Assistant
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## Run the application

```bash
streamlit run app.py
```

---

# 📌 Example Use Cases

- AI Research
- Technology Trend Analysis
- Academic Literature Exploration
- Market Research
- Company Analysis
- Product Research
- Competitive Intelligence

---

# 🎯 Future Enhancements

- Retrieval-Augmented Generation (RAG)
- PDF Research Support
- Multi-document Analysis
- Citation Verification
- Research Report Export (PDF)
- Conversation Memory
- Source Credibility Ranking
- Vector Database Integration (FAISS/ChromaDB)

---

# 👨‍💻 Author

**Ramanjot Singh**

- GitHub: https://github.com/Ramansahni
- LinkedIn: https://www.linkedin.com/in/ramanjot-singh-aa5b9327b/

---

# 📄 License

This project is licensed under the MIT License.

---

## ⭐ If you found this project useful, consider giving it a star!