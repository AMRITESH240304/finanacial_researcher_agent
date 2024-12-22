from crewai import Task
from .tools import tool,scrapeTool
from .agents import finance_researcher,final_researcher

finance_researcher_task = Task(
    description=(
        "Conduct financial research on the given topic: {topic} "
    ),
    agent=finance_researcher,
    expected_output="Clean and formatted financial data",
    tools=[tool, scrapeTool],
)

final_task = Task(
    description="Finalize the financial data.",
    agent=final_researcher,
    expected_output="provide me paragraph with all the necessary data",
)