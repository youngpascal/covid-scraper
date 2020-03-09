from flask import Flask
from scraper.models import Data, db_connect, JsonData
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
from flask import jsonify 
import json
def create_app(config=None, app_name=None):
    app = Flask(__name__)
    return app

app = Flask(__name__)

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