#!/usr/local/bin/python

import requests
import json

import os


DRONE_REPO_LINK = os.environ.get('DRONE_REPO_LINK')
DRONE_BUILD_LINK = os.environ.get('DRONE_BUILD_LINK')
DRONE_STAGE_NUMBER = os.environ.get('DRONE_STAGE_NUMBER')
DRONE_STEP_NUMBER = os.environ.get('DRONE_STEP_NUMBER')
DRONE_COMMIT_SHA = os.environ.get('DRONE_COMMIT_SHA')
DRONE_REPO = os.environ.get('DRONE_REPO')
GITEA_PAT = os.environ.get('GITEA_PAT')

_URL = DRONE_REPO_LINK.split('/')[2]

STATUS_URL = f'https://{_URL}/api/v1/repos/{DRONE_REPO}/statuses/{DRONE_COMMIT_SHA}'
BUILD_URL = f'{DRONE_BUILD_LINK}/{DRONE_STAGE_NUMBER}/{DRONE_STEP_NUMBER}'

AUTH_TOKEN = f'token {GITEA_PAT}'

status = {
    'context': f'testing/success',
    'target_url': BUILD_URL,
    'state': 'success',
    'description': 'test was successful'
}

HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': AUTH_TOKEN,
    'X-Script-name': 'success.py'
}

print(HEADERS)

data = requests.post(
    STATUS_URL,
    json=status,
    headers=HEADERS
)

print(data.status_code)
print(data.request.headers)
