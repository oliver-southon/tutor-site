##############################################################################
# AUTHOR: Oliver Southon                                                     #
# DATE: 21/02/2021                                                           #
# DESC: A flask app utilising sqlite3 to store a database of coding students #
############################################################################## 
from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
