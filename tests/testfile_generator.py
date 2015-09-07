import urllib.request
import sys
import os

# Download the file from `url` and save it locally under temp.py:
with urllib.request.urlopen(sys.argv[1]) as response, open('temp.py', 'wb') as output:
    data = response.read() # a `bytes` object
    output.write(data)

# import temp to get TEST values
from temp import TESTS
with open('test_auto_generated.py', 'wb') as output:
    output.write(b"""import unittest


class Tests(unittest.TestCase):""")

    for key in TESTS.keys():
        text = """

    def test_%s(self):""" % key
        output.write(text.encode('utf-8'))
        for test_entry in TESTS[key]:
            text = """
        assert checkio(%s) == %s""" % (test_entry['input'], test_entry['answer'])
            output.write(text.encode('utf-8'))

os.remove('temp.py')
