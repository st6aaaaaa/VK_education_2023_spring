def function(file_object, arr):
    set_words = set(map(lambda x: x.lower(), arr))
    if str(type(file_object)) != "<class '_io.TextIOWrapper'>":
        with open(file_object, "r") as file_pointer:
            while True:
                line = file_pointer.readline()
                if not line:
                    break
                tmp = set(line.lower().split())
                if tmp.intersection(set_words):
                    yield line.rstrip()
    else:
        while True:
            line = file_object.readline()
            if not line:
                break
            tmp = set(line.lower().split())
            if tmp.intersection(set_words):
                yield line.rstrip()
