from flask import Flask
from flask_cors import CORS

app = Flask(__name__, instance_relative_config=True)
CORS(app)

import data.router
