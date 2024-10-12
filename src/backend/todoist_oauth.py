from fastapi_controllers import Controller, get, post


class OAuthController(Controller):

    @get("/")
    def index(self):
        return {"message": "Hello from TodoistAiHelper."}

    @get("/oauth")
    def oauth(self):
        return {"message": "OAuth endpoint"}
