import requests
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

COWIN_URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode='


def retriveQueryForPin(pincode, date):
    date = date[-2:] +  "-" + date[5:7] + "-" + date[:4]
    print(date)
    url = COWIN_URL + pincode + '&date=' + date
    posts = requests.get(url, headers = {"Accept-Language": "hi_IN"})
    print(posts.json())
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

