from fastapi import APIRouter
from services.crew import crewKickOf
from services.groq_service import get_json
router = APIRouter()

@router.get("/")
async def hello_world():
    return {"message": "Hello, World!"}

@router.post("/crewkickoff")
async def crew_kickoff(input:str):
    result = crewKickOf(input)
    final_result = get_json(result.raw)
    return {"message": final_result}
