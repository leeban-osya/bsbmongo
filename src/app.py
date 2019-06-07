from flask import Flask, render_template
from src.common.mongo.database import Database

__author__ = 'nabee1'


app = Flask(__name__)
app.secret_key = '123'

@app.before_first_request
def init_db():
    Database.initialize()

@app.route('/')
def home():
    return render_template('home.jinja2')



from src.models.bsb.orders.views import bsborder_blueprint
app.register_blueprint(bsborder_blueprint, url_prefix="/bsborders")