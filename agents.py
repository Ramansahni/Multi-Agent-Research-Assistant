from langchain.agents import create_agent
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from tools import web_search, scrape_url

from dotenv import load_dotenv

load_dotenv()

llm = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0,
)


def build_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search],
    )


def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url],
    )


writer_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert research writer. Write clear, structured and insightful reports.",
        ),
        (
            "human",
            """Write a detailed research report on the topic below.

Topic:
{topic}

Research Gathered:
{research}

Structure:

- Introduction
- Key Findings (minimum 3 detailed points)
- Conclusion
- Sources (list all URLs)

Write professionally using markdown.
""",
        ),
    ]
)

writer_chain = writer_prompt | llm | StrOutputParser()


critic_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a strict research reviewer. Evaluate reports honestly.",
        ),
        (
            "human",
            """Review the report.

Report:
{report}

Return exactly:

Score: X/10

Strengths:
- ...

Areas to Improve:
- ...

One-line Verdict:
...
""",
        ),
    ]
)

critic_chain = critic_prompt | llm | StrOutputParser()