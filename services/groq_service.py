from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from config import settings
chat = ChatGroq(temperature=0, model_name="llama3-8b-8192",groq_api_key=settings.GROQ_API_KEY)

def get_json(crewinput:str):
    message = [
        (
            "system",
            "You are an expert in parsing financial data and converting it into structured JSON. Your task is to extract relevant financial data from the provided paragraph and organize it in a JSON format suitable for charting. "
            "Each key should represent the data type (e.g., 'Revenue', 'Net Income', 'Assets', 'Liabilities'), and the values should be arrays of objects containing the year and corresponding value. "
            "Ensure the JSON structure is clean and follows this format:\n\n"
            "{\n"
            "  'Revenue': [\n"
            "    { 'year': 2005, 'value': 1434.2 },\n"
            "    { 'year': 2006, 'value': 1734.1 },\n"
            "    ...\n"
            "  ],\n"
            "  'Net Income': [\n"
            "    { 'year': 2005, 'value': 241.2 },\n"
            "    { 'year': 2006, 'value': 341.1 },\n"
            "    ...\n"
            "  ],\n"
            "  'Assets': [...],\n"
            "  'Liabilities': [...]\n"
            "}\n\n"
            "Only return the JSON data, and ensure all numeric values are in millions (remove currency symbols)."
        ),
        ("user", crewinput)
    ]
    
    answer_json = chat.invoke(message)
    return answer_json

