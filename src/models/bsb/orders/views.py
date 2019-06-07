import json

from flask import Blueprint, render_template, request, redirect, url_for

from src.models.bsb.orders.order import BSBOrder

__author__ = 'nabee1'


bsborder_blueprint = Blueprint('bsborders', __name__)

@bsborder_blueprint.route('/')
def index():
    regions = BSBOrder.generate_regions_list()
    return render_template('BSBOrders/bsborder_index.jinja2', regions=regions)

@bsborder_blueprint.route('/bsborders_query_results', methods = ['POST', 'GET'])
def bsborders_query():
    if request.method == 'POST':
        # Splits input by commas, removes whitespaces and if element value is just empty string after comma split
        # then does not append it to list
        query_values_dict = dict((k, [x.strip() for x in v.split(",") if len(x.strip()) > 0]) for k, v in dict(request.form).items())
        print(query_values_dict)
        return render_template('BSBOrders/bsborders.jinja2', bsborders=BSBOrder.find_by_multiple_filters(query_values_dict), query=query_values_dict)
