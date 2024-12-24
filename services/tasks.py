from crewai import Task
from .tools import tool,scrapeTool
from .agents import finance_researcher,final_researcher,market_trends_analyst,chart_preparation_agent

finance_researcher_task = Task(
    description=(
        "Conduct in-depth financial research on the given topic: {topic}. Gather comprehensive data on financial status, historical market trends, quarterly financials, and controversies, ensuring the data is clean, accurate, and formatted for advanced analysis."
    ),
    agent=finance_researcher,
    expected_output="Cleaned, formatted, and detailed financial data ready for visualization and analysis",
    tools=[tool, scrapeTool],
)

market_trends_task = Task(
    description=(
        "Perform a detailed analysis of market trends for the specified sector: {topic}. Evaluate growth opportunities, competitive dynamics, consumer behavior, and emerging risks, providing actionable insights supported by robust data and visualizations."
    ),
    agent=market_trends_analyst,
    expected_output="A detailed report on market trends with actionable insights and visualizations",
    tools=[tool],
)

chart_preparation_task = Task(
    description="Prepare and structure data for visualization on topic:{topic}. Ensure the data is cleaned, annotated, and organized to enable seamless chart and graph generation using external tools.",
    agent=chart_preparation_agent,
    expected_output="Well-structured and annotated data ready for visualization",
    tools=[tool, scrapeTool],
)

final_task = Task(
    description="Consolidate and validate all financial and market data, ensuring accuracy and adherence to the provided Pydantic model. Deliver a structured and insightful final report tailored for strategic use.",
    agent=final_researcher,
    expected_output="A comprehensive and cohesive report with actionable insights and data visualizations",
)
