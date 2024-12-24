from fastapi import APIRouter
from services.crew import crewKickOf
from services.groq_service import get_json
from db.db import save_to_mongo,user_input
router = APIRouter()

@router.get("/")
async def hello_world():
    return {"message": "Hello, World!"}

@router.post("/crewkickoff")
async def crew_kickoff(input:str):
    result = crewKickOf(input)
    save_to_mongo(result.raw)
    final_result = get_json(result.raw)
    return {"crew_result": result, "final_result": final_result}

@router.post("/rag")
async def rag(input:str):
    return user_input(input)
