from crewai import Crew,Process
from .agents import finance_researcher,final_researcher
from .tasks import finance_researcher_task,final_task

crew=Crew(
    agents=[finance_researcher,final_researcher],
    tasks=[finance_researcher_task,final_task],
    process=Process.sequential,
    verbose=True
)

def crewKickOf(input:str):
    result=crew.kickoff(inputs={'topic':input})
    return result