from os import path
import random

CLIENT_ID = ''
with open(path.join(path.dirname(__file__), 'client_id.txt'), 'r') as file:
    CLIENT_ID = file.readline()

CLIENT_SECRET = ''
with open(path.join(path.dirname(__file__), 'client_secret.txt'), 'r') as file:
    CLIENT_SECRET = file.readline()

REDIRECT_URI = 'http://localhost:8080/oauth'

SCOPE = 'data:read_write'

STATE = 'wow'+str(random.randint(-1000, 1000))

URL = f'https://todoist.com/oauth/authorize?client_id={CLIENT_ID}&scope={SCOPE}&state={STATE}'
