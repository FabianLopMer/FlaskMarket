from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SQLALCHEMY_TRACK_MPDIFICATIONS'] = False
app.config['SECRET_KEY'] = '9e6f82af02025bfbfd1c9772'
db = SQLAlchemy(app)

'''' Si se pone antes del app=Flask--- no lo reconoce'''
from market import routes
