from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from flask_cors import CORS
from model import Log, Base
from helpers import insert_mock_data
import logging, sys, os, time

app = Flask(__name__)
CORS(app)

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

DATABASE_URI = os.environ.get('DATABASE_URI') 

# init db engine
engine = create_engine(DATABASE_URI)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
    
@app.route('/logs', methods=['GET'])
def get_logs():
    logs = Session().query(Log).all()
    log_list = [dict(id=log.id, ip=log.ip, datetime=log.datetime, 
                     request_method=log.request_method, path=log.path, 
                     status=log.status, size=log.size, 
                     referrer=log.referrer, user_agent=log.user_agent) for log in logs]
    return jsonify(log_list)

@app.route('/', methods=["GET"])
def index():
    app.logger.info("Hello World accessed")
     
    return "Hello, world"

if __name__ == '__main__':

    time.sleep(2) # wait for postgres server 
     
    Base.metadata.create_all(engine)

    session = Session()
    insert_mock_data(session, 1000)

    app.logger.info("\t Starting App")
    app.run(
        host="0.0.0.0",
        port=3001,
        debug=True,
        use_reloader=False
    )