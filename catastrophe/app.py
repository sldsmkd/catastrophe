import json
import requests
import string
from collections import defaultdict, UserDict, Counter
from flask import Flask

app = Flask(__name__)


class CatFacts(UserDict):

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

    def list_users(self):
        users = defaultdict(int)
        for fact in self.data:
            users[fact["user"]["_id"]] += 1
        return users

    def list_user_facts(self, id):
        user_facts = []
        for fact in self.data:
            if id == fact["user"]["_id"]:
                user_facts.append(fact["_id"])
        return user_facts

    def get_fact(self, id):
        for fact in self.data:
            if id == fact["_id"]:
                return fact["text"]

    def delete_fact(self, id):
        pass


cat_facts = CatFacts()


def formatter(output):
    if output is not None:
        response = app.response_class(response=json.dumps(output),
                                      status=200,
                                      mimetype='application/json')
    else:
        response = app.response_class(response="",
                                      status=404,
                                      mimetype='application/json')
    return response

@app.route('/users')
def users():
    return formatter(cat_facts.list_users())


@app.route('/user/<user_id>')
def user_facts(user_id):
    return formatter(cat_facts.list_user_facts(user_id))


@app.route('/fact/<fact_id>')
def fact(fact_id):
    return formatter(cat_facts.get_fact(fact_id))


@app.route('/')
def doc():
    doc = """
Hello World

    """
    return(doc)


app.run(host="0.0.0.0", port=5000)
