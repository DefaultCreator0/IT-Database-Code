# Filename - server.py

# Import flask and datetime module for showing date and time
from flask import Flask, request, jsonify
import datetime
from flask_cors import CORS, cross_origin
from AI import AIChat
import json

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})
Chatbot = AIChat()

DataPacket = []

DataPacket = Chatbot.SendUserRqst("Hello")
storedData ={"":""}

def SendRequest(Request):
    global DataPacket
    DataPacket = Chatbot.SendUserRqst(Request)
    #getAiInput()
    return DataPacket[1]


# Route for seeing a data
@app.route('/Fetch',methods={"GET"})
def getAiInput():
    # Returning an api for showing in  reactjs
    return DataPacket[1]

@app.route('/post',methods={"GET","POST"})
def sendUserInput():

    data = {"":""}
    # Process the data 
    
    try:
        if request.method == "POST":
            
            temp = json.loads(request.data.decode('utf-8').replace("'", '"'))
            global storedData
            storedData = {"Input" : temp["message"]}
            return SendRequest(temp["message"])
        if request.method == "GET":
            return storedData["message"]
    except:
        data = {"Data":"Empty"}
    return data
    





# Running app
if __name__ == '__main__':
    app.run(debug=True)

