from crewai import Crew,Process
from .agents import finance_researcher,final_researcher,market_trends_analyst,chart_preparation_agent
from .tasks import finance_researcher_task,final_task,market_trends_task,chart_preparation_task

crew=Crew(
    agents=[finance_researcher,market_trends_analyst,chart_preparation_agent,final_researcher],
    tasks=[finance_researcher_task,market_trends_task,chart_preparation_task,final_task],
    process=Process.sequential,
    verbose=True
)

def crewKickOf(input:str):
    result=crew.kickoff(inputs={'topic':input})
    return result