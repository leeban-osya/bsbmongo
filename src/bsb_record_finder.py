from src.models.bsb.orders.order import BSBOrder
from src.common.mongo.database import Database

Database.initialize()
"""
results = BSBOrder.find_by_orderDetailID("123225758")

for result in results:
    print(result.json())
"""

print(BSBOrder.generate_regions_list())