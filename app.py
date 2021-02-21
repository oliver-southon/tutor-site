##############################################################################
# AUTHOR: Oliver Southon                                                     #
# DATE: 21/02/2021                                                           #
# DESC: A flask app utilising sqlite3 to store a database of coding students #
############################################################################## 
from os import stat
from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addrec', methods=['GET', 'POST'])
def addrec():
    if request.method == 'POST':
        try:
            fnm = request.form['fnm']
            lnm = request.form['lnm']
            age = request.form['age']
            email = request.form['email']
            lang = request.form['lang']
            desc = request.form['desc']
            cm = request.form['cm']

            with sql.connect('peers.db') as conn:
                c = conn.cursor()
                c.execute("""
                INSERT INTO peer (
                    first_name, last_name, age, email, language, desc, contact_method
                )

                VALUES (?,?,?,?,?,?,?)
                """, (fnm,lnm,age,email,lang,desc,cm))
                conn.commit()
                conn.close()
                status = "Record successfuly added."
                print("added")
        except:
            conn.rollback()
            status = "Error adding record."
        finally:
            return render_template("result.html", msg=status)
            conn.close()
if __name__ == "__main__":
    app.run(debug=True)
