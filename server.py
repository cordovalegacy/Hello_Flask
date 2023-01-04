#
##We will need these lines each time in this order
from flask import Flask
app = Flask(__name__)
##
#


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/success')
def success():
    return "Success!"

#
##The code below allows us to use the name variable 
## INSIDE the URL, and pass through whatever that name is to the browser
@app.route('/hello/<first_name>/<last_name>/<age>')
def name_route(first_name, last_name, age):
    print(first_name, last_name, age)
    return f"Hello {first_name} {last_name}...My records indicate you are {age} years old!"
##
#

#
## app.run(debug=True) should be the very last statement!
if __name__=='__main__':
    app.run(debug = True)
##
#

#The code above will create a web server and additional routes (similar to server.js in MERN)

#
##
###pipenv install flask
###pipenv shell
##
#