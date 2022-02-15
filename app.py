from flask import Flask, render_template, request, flash, g
import sqlite3, random

# Create instance of Flask by calling its class constructor
app = Flask(__name__)
app.secret_key = "12ev@0947!fBjs8AA#4$32jHbd_sjhAdhc%mhn_773gvPPahG/HSI*IH_jbs"

# Main page
@app.route('/', methods=['GET'])
def index():
    flash("AFFIRMATION FOR TODAY!")
    return render_template("index.html")


@app.route('/affirmation', methods=['GET', 'POST'])
def affirmation():
    sentence = get_db()
    return render_template("index.html", sentence=sentence)


# Managing database connection
# g is to manage resources during a request
# During a request, every call to get_db() will return the same connection, 
# and it will be closed automatically at the end of the request

# this function is connecting our database to our application
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('affirmations_list.db')
        cursor = db.cursor()
        cursor.execute("select name from affirmations")
        all_data = cursor.fetchall() # keeps all names in tuples
        all_names = [str(val[0]) for val in all_data] # hold names only
        random_affirmation = random.choice(all_names)
    return random_affirmation

# this function is terminating our database connection
# once we are done with using it
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# run app
if __name__ == '__main__':
	app.run(debug=True)