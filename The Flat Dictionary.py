def flatten(dictionary):
    result = {}
    dicts = dictionary.copy()
    firstRound = True
    while firstRound or filter(lambda x: isinstance(x, dict), dicts.values()):
        tempDict = {}
        firstRound = False
        for key, value in dicts.items():
            if not isinstance(value, dict):
                tempDict[key] = value
            else:
                # nested dict
                if value:
                    for j in value:
                        tempDict[key + '/' + j] = value[j]
                # empty dict
                else:
                    tempDict[key] = ''
        result = tempDict.copy()
        dicts = result.copy()
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
        "first": "One",
        "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {
        "place": {
               "zone": "1",
               "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
