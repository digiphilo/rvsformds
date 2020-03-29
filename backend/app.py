import os
from flask import Flask
from flask import request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://rvsformds:rvs4mds44@localhost:5432/rvsformds')

db = SQLAlchemy(app)
CORS(app)

class Medic(db.Model):

    __tablename__ = 'medics'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    phone = db.Column(db.String())
    city = db.Column(db.String())
    state = db.Column(db.String())
    county = db.Column(db.String())
    zip = db.Column(db.String())
    other = db.Column(db.String())
    matched = db.Column(db.Boolean())

    def __init__(self, name, email, phone, city, state, county, zip, other, matched=False):
        self.name = name
        self.email = email
        self.phone = phone
        self.city = city
        self.state = state
        self.county = county
        self.zip = zip
        self.other = other
        self.matched = matched

    def __repr__(self):
        return '<Medic %s>' % self.name

class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    phone = db.Column(db.String())
    city = db.Column(db.String())
    state = db.Column(db.String())
    county = db.Column(db.String())
    zip = db.Column(db.String())
    rvtype = db.Column(db.String())
    other = db.Column(db.String())
    matched = db.Column(db.Boolean())

    def __init__(self, name, email, phone, city, state, county, zip, rvtype, other, matched=False):
        self.name = name
        self.email = email
        self.phone = phone
        self.city = city
        self.state = state
        self.county = county
        self.zip = zip
        self.rvtype = rvtype
        self.other = other
        self.matched = matched

    def __repr__(self):
        return '<Owner %s>' % self.name

@app.route('/')
def index():
    return 'rvs for mds'

@app.route('/medic_form', methods=['POST'])
def medic_form():
    form_data = (request.get_json())
    medic = Medic(name=form_data.get('name', ''),
                  email=form_data.get('email', ''),
                  phone=form_data.get('phone', ''),
                  city=form_data.get('city', ''),
                  state=form_data.get('state', ''),
                  county=form_data.get('county', ''),
                  zip=form_data.get('zip', ''),
                  other=form_data.get('other', ''))
    db.session.add(medic)
    db.session.commit()
    return 'ok'

@app.route('/owner_form', methods=['POST'])
def owner_form():
    form_data = (request.get_json())
    owner = Owner(name=form_data.get('name', ''),
                  email=form_data.get('email', ''),
                  phone=form_data.get('phone', ''),
                  city=form_data.get('city', ''),
                  state=form_data.get('state', ''),
                  county=form_data.get('county', ''),
                  zip=form_data.get('zip', ''),
                  rvtype=form_data.get('rvtype', ''),
                  other=form_data.get('other', ''))
    db.session.add(owner)
    db.session.commit()
    return 'ok'

@app.route('/admin')
def admin():
    return 'rvs for mds admin'
