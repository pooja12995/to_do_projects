from flask import Flask,request , jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import pymongo


load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
# Create a new client and connect to the server
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

db = client['tudetutorialdb']
collection = db['tudetutorial'] 

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

app = Flask(__name__) #instance create flask appliation

@app.route('/submit',methods=['POST']) #nothing to give name as variable
def submit():
    form_data = dict(request.json)
    collection.insert_one(form_data)
    return "Data submitted successfully!"

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=9000,debug=True) #for debug look for change and reflect to browser
    #app.run()