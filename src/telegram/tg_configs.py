from os import path

TOKEN = ''
with open(path.join(path.dirname(__file__), 'token.txt'), "r") as file:
    TOKEN = file.readline()

NOT_AUTH_ERROR_MESSAGE = "Oops. Seems you haven't registered yet. Call /start command for more details."
