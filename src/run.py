from src.app import app

__author__ = 'nabee1'

app.run(debug=app.config["DEBUG"], host='10.35.30.51', port='5000')