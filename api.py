import flask, requests, pycountry #Import needed libraries
#flask -> for the server
#requests -> to handle requests
#pycountry -> to get ISO 3166-1 alpha-2 code (situational)
from flask import request, jsonify, send_from_directory
#from te flask library, get these specific modules


#Set up the server
app = flask.Flask(__name__)
app.config["DEBUG"] = True


#Different 'sections' to the website, these two functions direct to the same page!
@app.route('/find/<path:path>')
def send_find_path(path): 
    return send_from_directory('pages/', path)

@app.route('/find/')
def send_find():
    return send_from_directory('pages', 'index.html')


#API segment of the backend
@app.route('/api/country', methods=['GET']) #This is a GET request, it converts country name into SO 3166-1 alpha-2 code
def getAlpha():
    input_country = request.args['id'] #This gets the query input and stores it in 'input-country' variable

    for country in pycountry.countries: #For each element (country) in pycountry.countries...
        if(country.name == input_country): #If the country name is equal to the query given (the country the user inputs)
            return country.alpha_2 #Simply return the ISO 3166-1 alpha-2 code
        
    return "ERROR" #Cannot find the country (user might have entered wrongly)


@app.route('/api/income', methods=['GET']) #This is also a GET request, it gets the SO 3166-1 alpha-2 code and sends info from worldbank API
def getIncome():
    alpha = request.args['id'] #Gets query input
    req = requests.get('http://api.worldbank.org/v2/country/' + alpha + '?format=json') #API call
    return req.text #Return it as a text, it gets processed as a json in the JS

app.run() #Run the app