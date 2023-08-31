# Created by: Ausar686
# https://github.com/Ausar686

import json

import requests

from why import why


def send_data(app):
	email = app.email
	lists = [test.data for test in app.tests[1:]]
	tests = why(lists, email)
	json_data = json.dumps(tests)
	url = 'http://crlab.site/wp-json/api/tests/results/add'
	r = requests.post(url, data={"json": json_data})
	return r