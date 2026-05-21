import os
from groq import Groq
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def call_groq(system: str, user: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ]
    )
    return response.choices[0].message.content.strip()

def research_agent(topic: str) -> str:
    console.print(Panel(f"[bold]Researching:[/bold] {topic}", style="blue"))

    # Step 1 — Planner Agent
    console.print("\n[yellow]Step 1 — Planner agent breaking down topic...[/yellow]")
    questions = call_groq(
        "You are a research planner. Break topics into key research questions.",
        f"Break this topic into 4 key research questions: {topic}\nReturn only the 4 questions, numbered."
    )
    console.print(f"[dim]{questions}[/dim]")

    # Step 2 — Research Agent
    console.print("\n[yellow]Step 2 — Research agent gathering findings...[/yellow]")
    findings = call_groq(
        "You are an expert researcher with deep knowledge across all domains.",
        f"Answer each of these research questions thoroughly with facts and examples:\n{questions}"
    )
    console.print(f"[dim]Findings gathered ✓[/dim]")

    # Step 3 — Analyst Agent
    console.print("\n[yellow]Step 3 — Analyst agent identifying insights...[/yellow]")
    insights = call_groq(
        "You are a senior analyst who identifies patterns and actionable insights.",
        f"Based on these findings about {topic}, identify 3 key insights and their implications:\n{findings}"
    )
    console.print(f"[dim]Insights extracted ✓[/dim]")

    # Step 4 — Writer Agent
    console.print("\n[yellow]Step 4 — Writer agent composing final report...[/yellow]")
    report = call_groq(
        "You are an expert report writer. Write clear, professional, structured reports.",
        f"""Write a professional research report on: {topic}

Use this research:
{findings}

And these insights:
{insights}

Format with these sections:
# {topic}
## Executive Summary
## Key Findings
## Key Insights
## Conclusion
"""
    )
    return report

if __name__ == "__main__":
    topic = input("\n🔬 Enter research topic: ")
    report = research_agent(topic)
    console.print("\n")
    console.print(Panel(Markdown(report), title="📋 Research Report", style="green"))
    
    # Save report
    with open("report.md", "w") as f:
        f.write(report)
    console.print("\n[dim]Report saved to report.md[/dim]")
