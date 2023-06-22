from flask import Flask, render_template, request
from sqlalchemy import asc
from db.shared import db, Database
import os
from db.models.lumber_transaction import LumberTransaction

app = Flask(__name__)

#Obtain absolute directory of this file 
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.config['INITIALIZED'] = False  # Flag to track initialization

def initialize_database():
    if not app.config['INITIALIZED']:
        with app.app_context():
            db.create_all()
            Database.clear_db(LumberTransaction)
            Database.populate_db(basedir+"/db/lumber.xlsx", LumberTransaction)
            app.config['INITIALIZED'] = True

initialize_database()

@app.get('/')
def main():
    #Obtain new form field or set to default, which is open using the request.args.get default value
    field = request.args.get('field',"open")
    return render_template('index.html', field=field,transactions=obtain_data(field))
    
def obtain_data(column_name):
    transactions_models = LumberTransaction.query.with_entities(LumberTransaction.date,getattr(LumberTransaction, column_name)).order_by(asc(LumberTransaction.date)).all()
    return [{'date': transaction.date.isoformat(), 'value': getattr(transaction, column_name)} for transaction in transactions_models]
