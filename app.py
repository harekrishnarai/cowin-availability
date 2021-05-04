import requests
from flask import Flask, render_template, request, redirect, url_for, jsonify
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin

app = Flask(__name__)

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('cowinUsers')

COWIN_URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode='

@app.route('/add', methods=['POST'])
@crossdomain(origin='*',headers=['access-control-allow-origin','Content-Type'])
def create():
  """
      create() : Add document to Firestore collection with request body.
      Ensure you pass a custom ID as part of json body in post request,
      e.g. json={'id': '1', 'title': 'Write a blog post'}
  """
  try:
      
      print(request.json)
      data = {
        'email': email,
        'pincode': pincode,
        'date': date
      }
      document_reference=db.collection('cowinUsers').document()
      document_reference.set(data)
      return _build_cors_prelight_response()
  except Exception as e:
      return f"An Error Occured: {e}"


def _build_cors_prelight_response():
 response = make_response()
 response.headers.add("Access-Control-Allow-Origin", "*")
 response.headers.add('Access-Control-Allow-Headers', "*")
 response.headers.add('Access-Control-Allow-Methods', "*")
 return response

def retriveQueryForPin(pincode, date):
    date = date[-2:] +  "-" + date[5:7] + "-" + date[:4]
    print(date)
    url = COWIN_URL + pincode + '&date=' + date
    posts = requests.get(url, headers = {"Accept-Language": "hi_IN"})
    print(posts.json())
    print(posts.headers)
    print(url)
    val = posts.json()
    return render_template('search.html', posts=val )

def retriveQueryForState(district, date):
    date = date[-2:] +  "-" + date[5:7] + "-" + date[:4]
    print(date)
    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=' + district + '&date=' + date
    posts = requests.get(url, headers = {"accept":"application/json", "Accept-Language": "hi_IN", "user-agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"})
    print(posts.json())
    print(url)
    val = posts.json()
    return render_template('search.html', posts=val )

@app.route('/',methods=['GET'])
def index():
    pincode = request.args.get('pincode')
    date = request.args.get('date')
    state = request.args.get('state')
    district = request.args.get('district')
    if pincode:
        return retriveQueryForPin(pincode, date)
    elif state:
        return retriveQueryForState(district, date)
    return render_template('home.html')

