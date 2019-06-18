from src.app import app

__author__ = 'nabee1'

app.run(debug=app.config["DEBUG"], host='localhost', port='5000')