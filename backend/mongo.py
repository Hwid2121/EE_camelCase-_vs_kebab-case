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
        user_val = res.user
        results_val = res.results
        print("User Data:", user_val)
        print("Results Data:", results_val)

        results_db = db['results']

        # Create a new document to be inserted into the database
        new_document = {
            "user": user_val.dict(),  # Convert Pydantic model to dict
            "results": [result.dict() for result in results_val]  # Convert each result item to dict
        }

        # Insert the new document into the database
        results_db.insert_one(new_document)
        print("result inserted in the db successfuly")

        # results_db.insert_one(res)


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
