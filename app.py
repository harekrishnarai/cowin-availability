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
      all_users = [doc.to_dict() for doc in usersRef.stream()]
      return jsonify(all_users), 200
  except Exception as e:
      return f"An Error Occured: {e}"

@app.route('/updateP', methods=['POST', 'PUT'])
def updateP():
    try:
        data = {
          'email': request.args.get('email'),
          'pincode': request.args.get('pincode'),
          'date': request.args.get('date'),
          'optin': request.args.get('optin'),
          'type': "1"
        }
        id = request.args.get('id')
        usersRef.document(id).update(data)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/updateD', methods=['POST', 'PUT'])
def updateD():
    try:
        data = {
          'email': request.args.get('email'),
          'district': request.args.get('district'),
          'date': request.args.get('date'),
          'optin': request.args.get('optin'),
          'type': "2"
        }
        id = request.args.get('id')
        usersRef.document(id).update(data)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/',methods=['GET'])
def index():
    return jsonify({"success": True}), 200


testusersRef = db.collection('testcowinUsers')
@app.route('/testList', methods=['GET'])
def testRead():
  try:
      all_testusers = [doc.to_dict() for doc in testusersRef.stream()]
      return jsonify(all_testusers), 200
  except Exception as e:
      return f"An Error Occured: {e}"


@app.route('/testUpdateD', methods=['POST', 'PUT'])
def testUpdateD():
    try:
        data = {
          'email': request.args.get('email'),
          'district': request.args.get('district'),
          'date': request.args.get('date'),
          'optin': request.args.get('optin'),
          'type': "2"
        }
        id = request.args.get('id')
        testusersRef.document(id).update(data)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/testUpdateP', methods=['POST', 'PUT'])
def testUpdateP():
    try:
        data = {
          'email': request.args.get('email'),
          'pincode': request.args.get('pincode'),
          'date': request.args.get('date'),
          'optin': request.args.get('optin'),
          'type': ""
        }
        id = request.args.get('id')
        testusersRef.document(id).update(data)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

