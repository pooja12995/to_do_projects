from flask import Flask,render_template,request
from datetime import datetime
import requests

BACKEND_URL = 'http://127.0.0.1:9000'
app = Flask(__name__) #instance create flask appliation

@app.route('/') #nothing to give /
def home():

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True) #for debug look for change and reflect to browser