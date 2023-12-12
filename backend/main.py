from fastapi import FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from mongo import get_db, insert_result_db, load_questions

from pydantic import BaseModel
from typing import List, Optional
from pydantic import BaseModel


app = FastAPI()
db = get_db()


# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Result(BaseModel):
    question: str
    time: str
    correct: str

class Item(BaseModel):
    Gender: Optional[str] = None
    Age: Optional[str] = None
    It_skills: Optional[str] = None
    Glasses: Optional[str] = None
    results: List[Result]

@app.get("/")
def home():
    return "Hello, World!"

@app.get("/test")
def test():
    return "Hello, test!"

@app.get("/questions")
async def retrieve_questions():
    print("Questions retrieved.")
    return load_questions()

@app.post("/results")
async def advanced_search(item: Item):
    print("Results transfered to the service.")
    insert_result_db(item)