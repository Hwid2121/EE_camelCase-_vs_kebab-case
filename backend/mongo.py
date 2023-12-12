import json
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# MongoDB Atlas connection string
uri = "mongodb+srv://experimentation:Exp123@ee.zr66ise.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['EE']



def insertResultDB(res):
    resultsDB = db['results']
    resultsDB.insert_one(res)
    print("Result added in the mongodb successfuly.")


def get_db():
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Successfully connected to MongoDB!")
        return client['EE']
    except Exception as e:
        print(e)
        return None

def insert_result_db(db, res):
    if db is not None:
        results_db = db['results']
        results_db.insert_one(res)


def load_questions():
    with open('questions.json', 'r') as file:
        data = json.load(file)
    return data


results_obj = {
    "Gender": "", 
    "Age": "",
    "it-skills": "", 
    "Glasses": "",
    "results": [{
        "question": "", 
        "time": "",
        "correct": ""
    }]
}
