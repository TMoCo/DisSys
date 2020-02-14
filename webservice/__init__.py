from flask import Flask
from .config import Config

app = Flask(__name__, template_folder='./web/templates', static_folder='./web/static')
app.config.from_object(Config)

from webservice.web import routes
