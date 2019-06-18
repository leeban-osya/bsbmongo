import json

from flask import Blueprint, render_template, request, redirect, url_for

from src.models.bsb.orders.order import BSBOrder
from src.models.bsb.orders.utils import handleRequestForm

__author__ = 'nabee1'


bsborder_blueprint = Blueprint('bsborders', __name__)

@bsborder_blueprint.route('/')
def index():
    regions = BSBOrder.generate_regions_list()
    return render_template('BSBOrders/bsborder_index.jinja2', regions=regions)

@bsborder_blueprint.route('/bsborders_query_results', methods = ['POST', 'GET'])
def bsborders_query():
    if request.method == 'POST':

        mongo_query = handleRequestForm(request.form, {
                                                        "orderDetailID": ["CommaString"],
                                                        "playerID": ["CommaString"],
                                                        "payment_Date_Start": ["DateString"],
                                                        "payment_Date_End": ["DateString"],
                                                        "region": ["DropdownString"]
                                                        })
        print(mongo_query)
        return render_template('BSBOrders/bsborders.jinja2', bsborders=BSBOrder.find_by_multiple_filters(mongo_query), query=mongo_query)
