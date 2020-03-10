from flask import Flask
from scraper.models import Data, db_connect, JsonData
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
from flask import jsonify 
from flask_heroku import Heroku
import json

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/pre-registration'



app = Flask(__name__)
heroku = Heroku(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



engine = db_connect()
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def index():
    res = session.query(JsonData.jsond).all()
    dump = []
    for rows in res:
        dump.append(json.loads(rows[0]))
    return jsonify(dump)

if __name__ == '__main__':
    app.run()