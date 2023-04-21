from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import time
import datetime
from db import addToDB 

app = Flask(__name__)
CORS(app, support_credentials = True)
@cross_origin(supports_credentials = True)

@app.route('/post', methods = ['POST'])
def post():
    data = json.loads(request.data)
    print(time.mktime(datetime.datetime.strptime(data["start-date"],
                                             "%Y/%m/%d").timetuple()))
    print(data)
    addToDB(data)

    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}


if __name__ == '__main__':
    app.run(debug = True)
