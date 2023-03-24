import json


def handler(field, word, string):
    return (field, word, string.count(word))


def parse_json(json_str, keyword_callback,
               required_fields=None, keywords=None):
    json_dict = json.loads(json_str)
    array = []

    if required_fields is None or keywords is None:
        return None

    for field in required_fields:
        if field in json_dict.keys():
            for word in keywords:
                if word in json_dict[field]:
                    temp = keyword_callback(field, word, json_dict[field])
                    array.append(temp)
    return array if array != [] else None
