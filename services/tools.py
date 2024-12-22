from config import settings
from crewai_tools import SerperDevTool,ScrapeWebsiteTool

print("Serper is ready to use")

tool = SerperDevTool(n_results=1)
scrapeTool = ScrapeWebsiteTool()