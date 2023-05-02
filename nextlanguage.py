import pymysql
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length, InputRequired

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy()
# create the app
app = Flask(__name__)
app.secret_key = 'tO$&!|0wkamvVia0?n$NqIRVWOG'

# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)
# Flask-WTF requires this line
csrf = CSRFProtect(app)

# assumes you did not create a password for your database
# and the database username is the default, 'root'
# change if necessary
username = 'andreari_kimchi'
password = ''
userpass = 'mysql+pymysql://' + username + ':' + password + '@'
server   = 'andrearivera.net'
# CHANGE to YOUR database name, with a slash added as shown
dbname   = '/andreari_next-language'


# CHANGE NOTHING BELOW
# put them all together as a string that shows SQLAlchemy where the database is
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# initialize the app with Flask-SQLAlchemy
db.init_app(app)


# NOTHING BELOW THIS LINE NEEDS TO CHANGE
# this route will test the database connection - and nothing more


class Language(db.Model):
    __tablename__ = 'languages'
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String)
    family = db.Column(db.String)
    branch = db.Column(db.String)
    writing = db.Column(db.String)
    speakers = db.Column(db.String)
    countries = db.Column(db.String)
    category = db.Column(db.String)
    weeks = db.Column(db.String)
    hours = db.Column(db.String)
    audio = db.Column(db.String)

class LangForm(FlaskForm):
    lang = RadioField('What language do you speak?', choices=[(47,'Chinese (Mandarin)'), (16,'English'),(64,'Spanish'),(29,'Hindi'),(2,'Arabic')], validators=[InputRequired()])
    #default=1, coerce=int,

    sort = RadioField('Filter by:', choices=[('family','Language family'), ('branch','Language Branch'),('writing','Writing system')], validators=[InputRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET'])
def index():
    try:
        form = LangForm()
        return render_template('index.html',form=form)

    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text



@app.route('/languages', methods=['POST'])
def result():
    lang_id = request.form['lang']
    sort_id = request.form['sort']






    return render_template('languages.html')





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4999, debug=True)
