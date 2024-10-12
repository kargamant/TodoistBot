from os import path

TOKEN = ''
with open(path.join(path.dirname(__file__), 'token.txt'), "r") as file:
    TOKEN = file.readline()
