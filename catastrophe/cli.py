#!../venv/bin/python
import argparse
import json
import requests
import yaml

api_endpoint = "http://localhost:5000"

parser = argparse.ArgumentParser(description='Get Cat Facts.')
parser.add_argument('method', help='users | user | fact')
parser.add_argument("-i", '--id', help='id')
parser.add_argument("-o", '--output', help='json|yaml')

args = parser.parse_args()

if args.method == "users":
    resp = requests.get(api_endpoint + "/users")

if args.method == "user":
    resp = requests.get(api_endpoint + "/user/" + args.id)

if args.method == "fact":
    resp = requests.get(api_endpoint + "/fact/" + args.id)

if (resp.status_code == 200):
    if args.output == "yaml":
        print(yaml.dump(resp.json()))
    else:
        print(resp.json())
else:
    print("Not Found")