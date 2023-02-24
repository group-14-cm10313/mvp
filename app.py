from flask import Flask, redirect, url_for, request
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/login',methods = ['POST'])
@cross_origin(supports_credentials=True)
def login():
      first_name = request.form['fname']
      last_name = request.form['lname']
      name_file = open("name.txt", "w")
      name_file.write(f"{first_name} {last_name}")
      name_file.close()
      return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
  

if __name__ == '__main__':
   app.run(debug = True)