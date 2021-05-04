import requests
from flask import Flask, request, jsonify
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
cors = CORS(app, resource={
r"/*":{
    "origins":"*"
}
})

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
usersRef = db.collection('cowinUsers')

@app.route('/addP', methods=['POST'])
def createP():
  try:
      data = {
        'email': request.form['email'],
        'pincode': request.form['pincode'],
        'date': request.form['date'],
        'optin': "1",
        'type': "1"
      }
      document_reference=db.collection('cowinUsers').document()
      document_reference.set(data)
      return jsonify({"success": "Subscribed Successfully"}), 200
  except Exception as e:
      return f"An Error Occured: {e}"

@app.route('/addD', methods=['POST'])
def createD():
  try:
      data = {
        'email': request.form['email'],
        'district': request.form['district'],
        'date': request.form['date'],
        'optin': "1",
        'type': "2"
      }
      document_reference=db.collection('cowinUsers').document()
      document_reference.set(data)
      return jsonify({"success": "Subscribed Successfully"}), 200
  except Exception as e:
      return f"An Error Occured: {e}"


@app.route('/list', methods=['GET'])
def read():
  try:
      # Check if ID was passed to URL query
      all_users = [doc.to_dict() for doc in usersRef.stream()]
      return jsonify(all_users), 200
  except Exception as e:
      return f"An Error Occured: {e}"


@app.route('/',methods=['GET'])
def index():
    return jsonify({"success": True}), 200
