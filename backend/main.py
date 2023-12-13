from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel

from mongo import get_db, insert_result_db, load_questions

app = FastAPI()
db = get_db()

# Enable CORS
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionResult(BaseModel):
    selectedOption: str
    time: str

class QuestionItem(BaseModel):
    sentence: str
    options: List[str]
    results: QuestionResult
    type: str

class User(BaseModel):
    age: Optional[str] = None
    consent: Optional[bool] = None
    gender: Optional[str] = None
    hasItSkills: Optional[bool] = None
    usesGlasses: Optional[bool] = None

class Item(BaseModel):
    user: User
    results: List[QuestionItem]

@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/test")
def test():
    return {"message": "Hello, test!"}


@app.post("/results")
async def post_results(item: Item):
    print("Results transferred to the service.", item)
    insert_result_db(db, item)
    return {"status": "success"}

@app.get("/questions")
async def retrieve_questions():
    print("Questions retrieved.")
    return load_questions()
