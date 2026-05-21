# 🔬 AI Research Agent

A multi-agent AI system that researches any topic and generates a structured professional report — with a live Streamlit UI and PDF export.

**🚀 Live demo:** https://ai-research-agent-63f9vvrbfmhtrzgmgwkwad.streamlit.app/

---

## What it does (non-technical)

Think of it like hiring a research team:
- You give them a topic
- One person plans the research questions
- Another digs into the answers
- A third finds the patterns
- A fourth writes the final report

Except all 4 are AI agents and the whole thing takes under 60 seconds.

---

## Architecture

User Input → Planner Agent → Research Agent → Analyst Agent → Writer Agent → PDF + Markdown Export

Each agent receives the previous agent's output as input — a sequential dependency chain.

---

## Tech Stack

| Component | Technology | Purpose |
|---|---|---|
| LLM | LLaMA 3.3 70B via Groq | Powers all 4 agents |
| Inference | Groq API | Ultra-fast free inference |
| UI | Streamlit | Web interface |
| PDF export | fpdf2 | Professional report generation |
| Language | Python 3.13 | Core orchestration |
| Deployment | Streamlit Cloud | Free live hosting |

---

## Why multi-agent instead of one LLM call?

A single LLM call produces generic output. Multi-agent forces specialization:

- Planner thinks about what to research — not what to write
- Researcher focuses purely on gathering information — no opinion
- Analyst focuses purely on patterns — no writing
- Writer focuses purely on communication — no research

One agent, one job. Output quality is significantly higher than a single prompt.

---

## Agent Prompts

Planner: "You are a research planner. Break topics into key research questions."
Researcher: "You are an expert researcher with deep knowledge across all domains."
Analyst: "You are a senior analyst who identifies patterns and actionable insights."
Writer: "You are an expert report writer. Write clear, professional, structured reports."

---

## Key Technical Decisions

Why Groq over OpenAI?
Groq runs LLaMA 3.3 70B at ~500 tokens/second — roughly 10x faster than OpenAI at zero cost. OpenAI-compatible API means switching back is a one-line change.

Why Streamlit over Flask/FastAPI?
st.status() shows real-time agent progress — critical UX when each step takes 3-5 seconds. Shipped a live deployed product in under an hour.

Why sequential agents instead of parallel?
Each agent depends on the previous agent's output. Sequential is the correct pattern — parallel would break the dependency chain.

Why fpdf2 for PDF?
Lightweight, pure Python, no browser engine required. Full layout control without the overhead of WeasyPrint or headless Chrome.

---

## 5W-1H

WHO: Analysts, students, professionals who need structured research fast
WHAT: Converts any topic into a professional report using 4 specialized AI agents
WHERE: Live on Streamlit Cloud — no install needed
WHEN: Before a meeting, writing a proposal, entering a new domain
WHY: Specialization produces better output than a single generalist prompt
HOW: Groq API → LLaMA 3.3 70B → 4 chained agents → Streamlit UI → PDF export

---

## Interview Q&A

Q: Why did you build this?
A: I wanted a project that demonstrates the full agentic pipeline in a way anyone can see running live. Most AI projects are scripts. This is a deployed product.

Q: How is this different from just asking ChatGPT?
A: ChatGPT is one generalist. This is four specialists. Specialization at the prompt level produces structured, higher-quality output — and the pipeline is auditable step by step.

Q: What would you add next?
A: Web search integration so agents use live data, a memory layer so research persists across sessions, and a citation tracker so every claim links to a source.

Q: How does the PDF generation work?
A: fpdf2 processes the markdown report line by line — headers get larger bold fonts, bullet points get indented, body text wraps. clean_text() strips markdown syntax and handles encoding before passing to fpdf.

Q: What was the hardest part?
A: PDF generation — fpdf2 throws a not enough horizontal space error when a word is wider than the page margin. Fixed by increasing margins, stripping bold markdown syntax, and encoding text to latin-1.

Q: How would you scale this for clinical research at Velocity?
A: Replace Groq knowledge with a RAG layer over clinical trial documents. Add web search pulling live data from ClinicalTrials.gov. Add a compliance agent that validates report content against regulatory guidelines before delivery.

---

## How to Run Locally

git clone https://github.com/SimhasGit/ai-research-agent.git
cd ai-research-agent
pip install -r requirements.txt
streamlit run app.py

Add your free Groq API key in the sidebar at console.groq.com.

---

## Project Structure

app.py — Streamlit UI + 4-agent pipeline
agent.py — CLI version for terminal use
requirements.txt — groq, streamlit, fpdf2, rich
README.md — Full project documentation
.gitignore — Excludes .env, cache, generated reports

---

## What I Learned

- Multi-agent prompt design — one job per agent produces better output than multi-role prompts
- Streamlit deployment — st.status() for real-time agent progress UX
- PDF generation edge cases — encoding, margin calculation, markdown stripping
- Groq API — OpenAI-compatible, 10x faster, free tier sufficient for demos
- The difference between a script and a deployed product
