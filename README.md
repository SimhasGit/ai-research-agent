# AI Research Agent

Live demo: https://ai-research-agent-63f9vvrbfmhtrzgmgwkwad.streamlit.app/

## What it does

4 AI agents collaborate to research any topic and generate a structured report in under 60 seconds.

User Input → Planner → Researcher → Analyst → Writer → PDF Export

## Tech Stack

- LLM: LLaMA 3.3 70B via Groq
- UI: Streamlit
- PDF: fpdf2
- Language: Python 3.13
- Deployment: Streamlit Cloud

## Why 4 agents instead of 1?

One agent, one job. Specialization at the prompt level produces better output than a single generalist prompt.

- Planner: breaks topic into research questions
- Researcher: answers each question in depth
- Analyst: extracts key patterns and insights
- Writer: composes the final structured report

## Agent Prompts

Planner: You are a research planner. Break topics into key research questions.
Researcher: You are an expert researcher with deep knowledge across all domains.
Analyst: You are a senior analyst who identifies patterns and actionable insights.
Writer: You are an expert report writer. Write clear, professional, structured reports.

## Key Technical Decisions

Why Groq over OpenAI?
Groq runs LLaMA 3.3 70B at 500 tokens/second — 10x faster than OpenAI at zero cost. OpenAI-compatible API means switching back is a one-line change.

Why sequential agents instead of parallel?
Each agent depends on the previous output. Parallel would break the dependency chain.

Why Streamlit?
st.status() shows real-time agent progress. Shipped a live deployed product in under an hour.

Why fpdf2?
Pure Python, no browser engine, full layout control.

## 5W-1H

WHO: Anyone who needs structured research fast
WHAT: Topic in, professional report out — via 4 specialized AI agents
WHERE: Live on Streamlit Cloud
WHEN: Before meetings, proposals, entering a new domain
WHY: Specialization produces better output than one generalist prompt
HOW: Groq API → LLaMA 3.3 70B → 4 chained agents → PDF

## Interview Q&A

Q: Why did you build this?
A: Most AI projects are scripts. I wanted a deployed product that shows the full agentic pipeline live.

Q: How is this different from ChatGPT?
A: ChatGPT is one generalist. This is four specialists. The pipeline is auditable step by step.

Q: What would you add next?
A: Web search for live data, memory layer for persistent research, citation tracker per claim.

Q: What was hardest?
A: PDF generation. fpdf2 throws a horizontal space error on long words. Fixed by increasing margins, stripping markdown bold syntax, and encoding to latin-1.

Q: How would you scale this for Velocity?
A: Add RAG over clinical trial documents, web search from ClinicalTrials.gov, and a compliance agent that validates against regulatory guidelines.

## How to Run

git clone https://github.com/SimhasGit/ai-research-agent.git
cd ai-research-agent
pip install -r requirements.txt
streamlit run app.py

## What I Learned

- One agent one job produces better output than multi-role prompts
- st.status() is the right Streamlit component for real-time agent UX
- fpdf2 edge cases around encoding and margins
- Groq is OpenAI-compatible and 10x faster for free
- The gap between a script and a deployed product
