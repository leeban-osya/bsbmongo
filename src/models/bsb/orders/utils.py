def handleRequestForm(request_form, transform_field_config):
    """
    Handles POST/GET data from user who is trying to filter BSB data,
    Transform config will specify what transforms should happen to what fields,
    returns appropriate mongodb query which will get user intended data.
    :param http_query: dict, transform_field_config: dict
    :return: mongo_query: dict
    """

    input_query = dict(request_form)
    mongo_query = {"$and": list()}

    print(input_query)
    mongo_date_queries = {}
    for fieldName,fieldData in input_query.items():
        mongo_field_query = str(fieldData[0])
        if len(mongo_field_query) < 1: continue
        for transform in transform_field_config[fieldName]:
            if transform == "CommaString":
                mongo_field_query = handleCommaString(mongo_field_query)
            if transform == "DateString":
                mongo_field_query = mongo_field_query
            if transform == "DropownString":
                mongo_field_query = mongo_field_query

        if fieldName in ["playerID", "orderDetailID"]:
            if len(mongo_field_query) > 0:
                mongo_query["$and"].append({fieldName: {
                                                        "$in": mongo_field_query
                                                         }
                                            })

        if fieldName in ["region"]:
            if mongo_field_query != "None":
                mongo_query["$and"].append({fieldName: {
                                                        "$in": [mongo_field_query]
                                                        }})

        if fieldName in ["payment_Date_Start", "payment_Date_End", "order_Date_Start", "order_Date_End"]:
            dateFieldMeta = fieldName.split("_")
            dateType, dateStartEnd = dateFieldMeta[0]+"Date", dateFieldMeta[2]
            mongo_date_queries[dateType] = mongo_date_queries.get(dateType, dict())

            if dateStartEnd == "Start":
                mongo_date_queries[dateType]["$gte"] = mongo_field_query
            if dateStartEnd == "End":
                mongo_date_queries[dateType]["$lt"] = mongo_field_query

    for k,v in mongo_date_queries.items():
        if len(mongo_query["$and"]) > 0:
            mongo_query["$and"].append({k:v})

    if len(mongo_query["$and"]) < 1:
        mongo_query.pop("$and")
        for k,v in mongo_date_queries.items():
            mongo_query[k] = mongo_date_queries[k]

    print(mongo_date_queries)
    print(mongo_query)
    return mongo_query
"""
playerID_query_dict = {"$in": query_values_dict['playerID']} if (len(query_values_dict['playerID']) > 0) else {'discard': True}
orderDetailID_query_dict = {"$in": query_values_dict['orderDetailID']} if (len(query_values_dict['orderDetailID']) > 0) else {'discard': True}
region_query_dict = {"$in": query_values_dict['region']} if not (query_values_dict['region'][0] == 'None') else {'discard': True}
paymentsDates_query_dict = {"$gte": query_values_dict["dateStart"][0] if (len(query_values_dict["dateStart"]) > 0) else {'discard': True},
                            "$lt": query_values_dict["dateEnd"][0] if (len(query_values_dict["dateStart"]) > 0) else {'discard': True}
                            }
                            
{
"$and": [
  {'playerID': playerID_query_dict},
  {'orderDetailID': orderDetailID_query_dict},
  {'region': region_query_dict},
  {'paymentDate': paymentsDates_query_dict}
]
}
"""


def handleCommaString(comma_string):
    """
    Takes input string for a field with multiple values seperated by commas,
    return a list of valid strings. Gets rid of white space and handles invalid inputs.
    :param comma_string: str
    :return: list_of_str
    """
    return [x.strip() for x in comma_string.split(",") if len(x.strip()) > 0]


