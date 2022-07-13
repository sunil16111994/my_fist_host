from unittest import result
from flask import *

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/sunil/<int:name>')
def fun_name(name):
    if name == 1428:
        result = {
            "name": "Sushma",
            "usn":name,
            "city":"Bangalore"
        }
    elif name == 1040:
        result = {
            "name": "Kavitha",
            "usn":name,
            "city":"Bangalore"
        }
    else:
        result = {
            "name": "Result not found"
        }
    return result

if __name__ == "__main__":
    app.run(debug=True)
