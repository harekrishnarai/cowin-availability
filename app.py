import requests
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

COWIN_URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode='

def retriveQuery(pincode, date):
    url = COWIN_URL + pincode + '&date=' + date
    posts = requests.get(COWIN_URL)
    return render_template('search.html', posts=posts)


@app.route("/")
def index():
    pincode = request.args.get('pincode')
    date = request.args.get('date')
    if pincode:
        return retriveQuery(pincode, date)
    return render_template('home.html')

