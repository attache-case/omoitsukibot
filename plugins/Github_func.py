# coding: utf-8

import json
import requests

# Authentication for user filing issue (must have read/write access to
# repository to add issue to)
USERNAME = 'CHANGEME'
PASSWORD = 'CHANGEME'

# The repository to add this issue to
REPO_OWNER = 'IIS-Lab'
REPO_NAME = 'LightBulb'

def make_github_issue(title, body=None, assignee=None, milestone=None, labels=[]):
	'''Create an issue on github.com using the given parameters.'''
	# Our url to create issues via POST
	url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
	# Create an authenticated session to create the issue
	session = requests.Session()
	session.auth = (USERNAME, PASSWORD)
	# Create our issue
	issue = {'title': title,
			'body': body,
			'assignee': assignee,
			'milestone': milestone,
			'labels': labels}
	# Add the issue to our repository
	r = session.post(url, json.dumps(issue))
	if r.status_code == 201:
		print('Successfully created Issue "{0}"'.format(title))
	else:
		print('Could not create Issue "{0}"'.format(title))
		print('Response:'+ r.content)