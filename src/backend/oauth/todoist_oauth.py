from fastapi_controllers import Controller, get, post
import requests
from .environments import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

class OAuthController(Controller):

    @get("/")
    def index(self):
        return {"message": "Hello from TodoistAiHelper."}

    @get("/oauth")
    def oauth(self, code, state):
        response = requests.post("https://todoist.com/oauth/access_token", params={
            'client_id' : CLIENT_ID,
            'client_secret' : CLIENT_SECRET,
            'code' : code,
            'redirect_uri' : REDIRECT_URI
        })
        print(response.json())
        return response.json() # just for now
