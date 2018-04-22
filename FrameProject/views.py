"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from FrameProject import app
from flask import jsonify


@app.route('/')
@app.route('/home')
def home():
    """
        Serve first page - page with the buttons
    """
    return render_template('FirstPage.html')

@app.route('/getjson')
def getJson():
    """
        Received: None
        Returned: JSON
    """
    return  jsonify(username="MEME",email="example@email.com")


@app.route('/getname', methods=['POST'])
def getName():
    """
        Received: JSON
        Returned: String - the json field 'name' is returned back
    """
    x = request.values
    return x['name']






