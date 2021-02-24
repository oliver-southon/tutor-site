##############################################################################
# AUTHOR: Oliver Southon                                                     #
# DATE: 21/02/2021                                                           #
# DESC: A flask app utilising sqlite3 to store a database of coding students #
############################################################################## 
import os
from flask import Flask, render_template, request
import sqlite3 as sql
from flask_bootstrap import Bootstrap
from model import ContactForm
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = str(os.environ.get('DB_DK'))
Bootstrap(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    form = ContactForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        fnm = form.firstName.data
        lnm = form.lastName.data
        email = form.email.data
        lang = form.primLang.data
        desc = form.desc.data
        date = datetime.datetime.now()

        with sql.connect('peers.db') as conn:
                c = conn.cursor()
                c.execute("""INSERT INTO peer 
                (first_name, last_name, email, language, desc, date) VALUES (?,?,?,?,?,?)""", 
                (fnm, lnm, email, lang, desc, date))
                conn.commit()
                status = "Record successfuly added."
                print("added")
        return 'Registration confirmed'
    return render_template('index.html', form=form)

@app.route('/addrec', methods=['GET', 'POST'])
def addrec():
    if request.method == 'POST':
        try:
            fnm = request.form['firstName']
            lnm = request.form['lastName']
            email = request.form['email']
            primLang = request.form['primLang']
            desc = request.form['desc']

            with sql.connect('peers.db') as conn:
                c = conn.cursor()
                c.execute("""
                INSERT INTO peer (
                    first_name, last_name, email, language, desc
                )

                VALUES (?,?,?,?,?)
                """, (fnm,lnm,email,primLang,desc,))
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
