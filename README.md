# Sending post request from HTML form to python backend, which then writes data to a form

## Breaking down elements

There are two important files here:

1. app.py - hold python app
2. index.html - holds website code

### app.py

First, we import eventhing we need
    from flask import Flask, redirect, url_for, request
    from flask_cors import CORS, cross_origin
    import json
    
To get this to work on your computer, you must first check if you have python - if you don't then install it here https://www.python.org/downloads/
Then run this command:

    pip install flask flask_cors json
    
Next, we create the app and allow CORS (cross origin resource sharing - basically tells the flask app that it's cool to accept data from our form)

    app = Flask(__name__)
    CORS(app, support_credentials=True)
    
After we have defined our app, we make a POST route at the /login route, this extracts the data from the request into first_name and last_name, opens a file, writes to it and the closes the file

    @app.route('/login',methods = ['POST'])
    @cross_origin(supports_credentials=True)
    def login():
          first_name = request.form['fname']
          last_name = request.form['lname']
          name_file = open("name.txt", "w")
          name_file.write(f"{first_name} {last_name}")
          name_file.close()
          return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

This last little bit tells python that if the file is called, run the flask app

    if __name__ == '__main__':
       app.run(debug = True)
       
# Getting started

To get this demo to work, you need to open the html file in your web browser of choice (google chrome is best imo) and start the python app either by running

    python app.py
 
or clicking run in the python IDLE with the file open.


Then submit the html form by pressing submit here:

![image](https://user-images.githubusercontent.com/62213643/221173214-f7557ef8-438a-477a-9003-360265b20a2f.png)

and look in your python console to see this output:

![image](https://user-images.githubusercontent.com/62213643/221173288-164e1c96-a467-4780-b776-654c3e6bc9f6.png)

Then check the place your files are for this project, and python should have created a file called name.txt which looks like this:

![image](https://user-images.githubusercontent.com/62213643/221173402-e68a6932-da20-42f2-976b-e82a3979adc7.png)

![image](https://user-images.githubusercontent.com/62213643/221173440-29b78829-f99b-4d3a-b43f-2a947568a3d1.png)


