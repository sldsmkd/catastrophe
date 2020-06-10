import collections
import json
import requests
import string
from flask import Flask

app = Flask(__name__)


class CatFacts(collections.UserDict):

    def _filter_facts(self, fact):
        filter = string.ascii_uppercase[::2]
        try:
            if fact['user']['name']['first'][0] in filter:
                return fact
        except KeyError:
            return None

    def __init__(self):
        url = 'https://cat-fact.herokuapp.com/facts'
        r = requests.get(url)
        facts = r.json()
        self.data = [fact for fact in facts['all'] if self._filter_facts(fact)]


cat_facts = CatFacts()


@app.route('/')
def hello_world():
    return 'Hello, World!'

app.run(host="0.0.0.0", port=5000)
