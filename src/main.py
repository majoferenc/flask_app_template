from datetime import datetime
from flask import Flask, jsonify
# Flask CORS is needed for enabling serving requests from all hostnames
from flask_cors import CORS, cross_origin

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from demo_entity import DemoEntity
from base_factory import Base
from entry_logger import logger
import logging
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('-debugMode', '--debugMode', help='Turn on debug mode, default: False', type=bool, required=False,
                    default=False)
parser.add_argument('-logToFile', '--logToFile', help='Turn on logging to file, default: False', type=bool, required=False,
                    default=False)
parser.add_argument('-logLevel', '--logLevel', help='Set Log Level, default: INFO', type=str, required=False,
                    default='INFO')
parser.add_argument('-port', '--port', help='Set App listen port, default: 8080', type=int, required=False,
                    default=8080)
parser.add_argument('-host', '--host', help='Set App listen host address, default: 0.0.0.0', type=str, required=False,
                    default='0.0.0.0')

log_levels = {
    'critical': logging.CRITICAL,
    'error': logging.ERROR,
    'warn': logging.WARNING,
    'warning': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG
}

args = parser.parse_args()

log_level = log_levels.get(args.logLevel.lower())

if args.logToFile:
    logging.basicConfig(filename= datetime.now().strftime('%Y_%m_%d.log'), level=log_level, format="%(asctime)s: %(levelname)s: %(message)s")
else:
    logging.basicConfig(level=log_level, format="%(asctime)s: %(levelname)s: %(message)s")

_DB_URI = 'sqlite:///test.db'
engine = create_engine(_DB_URI, echo=True)

DBSession = sessionmaker(bind=engine)
session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base.query = session.query_property()
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
@logger
def index():
    result = DemoEntity.query.all()
    result_json = []
    for element in result:
        result_json.append(element.toJSON())
        logging.info(element.toJSON())
    return result_json

@app.before_first_request
@logger
def create_tables():
    Base.metadata.create_all(engine, checkfirst=True)
    test_instance = DemoEntity(firstname='Ahoj', lastname='Cau')
    session.add(test_instance)
    session.commit()
    session.flush()


# main entrypoint of the flask app
if __name__ == '__main__':
    logging.info('Starting Application')
    app.run(host=args.host, port=args.port, debug=args.debugMode)
