mport json


def handler(field, word):
    # реализация не важна
    pass


def parse_json(json_str, keyword_callback=None,
               required_fields=None, keywords=None):

    json_dict = json.loads(json_str)

    if required_fields is None or keywords is None or \
            keyword_callback is None:
        pass
    else:
        for field in required_fields:
            if field in json_dict.keys():
                for word in keywords:
                    if word in json_dict[field].split():
                        keyword_callback(field, word)
                        
