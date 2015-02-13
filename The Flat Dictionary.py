def flatten(a):
    if a:
        result = {}
        for i in a:
            if isinstance(a[i], dict):
                temp = flatten(a[i])
                if temp:
                    for j in temp:
                        result['%s/%s' % (i, j)] = temp[j]
                else:
                    result[i] = ''
            else:
                result[i] = a[i]
        return result
    else:
        return None


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
