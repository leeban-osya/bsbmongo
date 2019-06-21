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

    print("raw_input", input_query)
    mongo_date_queries = {}
    mongo_name_queries = {}
    for fieldName, fieldData in input_query.items():
        #print(fieldName)
        mongo_field_query = str(fieldData)
        if len(mongo_field_query) < 1:
            continue
        for transform in transform_field_config[fieldName]:
            if transform == "CommaString":
                mongo_field_query = handleCommaString(mongo_field_query)
            if transform == "DateString":
                mongo_field_query = handleDateString(mongo_field_query)
            if transform == "DropdownString":
                mongo_field_query = handleDropdownString(mongo_field_query)

        if fieldName in ["playerID", "orderDetailID"]:
            if len(mongo_field_query) > 0:
                mongo_query["$and"].append({fieldName: {
                                                        "$in": mongo_field_query
                                                         }
                                            })

        if fieldName in ["region"]:
            if mongo_field_query != "All Regions":
                mongo_query["$and"].append({fieldName: {
                                                        "$in": [mongo_field_query]
                                                        }})

        if fieldName in ["playerName", "userName"]:
            print(fieldName, mongo_field_query)
            nameType = fieldName.split("Name")[0]
            mongo_name_queries[nameType] = mongo_name_queries.get(nameType, {
                "FirstName": list(),
                "LastName": list()
            })
            for name_query in mongo_field_query:
                if len(name_query.split(" ")) > 1:
                    firstName, lastName = " ".join(name_query.split(" ")[:-1]), name_query.split(" ")[-1]
                    mongo_name_queries[nameType]["FirstName"].append(firstName)
                    mongo_name_queries[nameType]["LastName"].append(lastName)
                else:
                    lastName = name_query
                    mongo_name_queries[nameType]["LastName"].append(lastName)

        if fieldName in ["payment_Date_Start", "payment_Date_End", "order_Date_Start", "order_Date_End"]:
            dateFieldMeta = fieldName.split("_")
            dateType, dateStartEnd = dateFieldMeta[0]+"Date", dateFieldMeta[2]
            mongo_date_queries[dateType] = mongo_date_queries.get(dateType, dict())

            if dateStartEnd == "Start":
                mongo_date_queries[dateType]["$gte"] = mongo_field_query
            if dateStartEnd == "End":
                mongo_date_queries[dateType]["$lt"] = mongo_field_query

    print(mongo_name_queries)
    if len(mongo_name_queries) > 0:
        for k, v in mongo_name_queries.items():
            for key, val in v.items():
                if len(val) > 0:
                    mongo_query["$and"].append({k+key: {
                                                        "$in": val
                                                        }})
    for k, v in mongo_date_queries.items():
        if len(mongo_query["$and"]) > 0:
            mongo_query["$and"].append({k:v})

    if len(mongo_query["$and"]) < 1:
        mongo_query.pop("$and")
        for k,v in mongo_date_queries.items():
            mongo_query[k] = mongo_date_queries[k]

    print("mongo_query", mongo_query)
    return mongo_query



def handleCommaString(comma_string):
    """
    Takes input string for a field with multiple values seperated by commas,
    return a list of valid strings. Gets rid of white space and handles invalid inputs.
    :param comma_string: str
    :return: list_of_str
    """
    return [x.strip() for x in comma_string.split(",") if len(x.strip()) > 0]

def handleDateString(date_string):
    return date_string

def handleDropdownString(dropdown_string):
    return dropdown_string

