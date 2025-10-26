
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from main import get_research_response

app = FastAPI()

class ResearchQuery(BaseModel):
    query: str

@app.post("/research")
async def research(query: ResearchQuery):
    response = get_research_response(query.query)
    return response

app.mount("/", StaticFiles(directory="static", html=True), name="static")
