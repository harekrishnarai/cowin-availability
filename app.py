import requests
from flask import Flask, request, jsonify
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
usersRef = db.collection('cowinUsers')

@app.route('/addP', methods=['POST'])
@cross_origin()
def create():
  try:
      data = {
        'email': request.form['email'],
        'pincode': request.form['pincode'],
        'date': request.form['date'],
        'optin': "1"
      }
      document_reference=db.collection('cowinUsers').document()
      document_reference.set(data)
      return jsonify({"success": True}), 200
  except Exception as e:
      return f"An Error Occured: {e}"

@app.route('/addD', methods=['POST'])
@cross_origin()
def create():
  try:
      data = {
        'email': request.form['email'],
        'district': request.form['district'],
        'date': request.form['date'],
        'optin': "1"
      }
      document_reference=db.collection('cowinUsers').document()
      document_reference.set(data)
      return jsonify({"success": True}), 200
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
