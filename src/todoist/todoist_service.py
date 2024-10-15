import todoist_api_python.api as td
from .todoist_config import GREETINGS_TASK_TEXT
from requests.exceptions import HTTPError


async def verify_token(access_token: str) -> True | False:
    try:
        api = td.TodoistAPI(access_token)
    except HTTPError:
        return False
    return True


class TodoistService:
    def __init__(self, access_token: str):
        self.api = td.TodoistAPI(access_token)

    def drop_greetings(self):
        self.api.add_task(content=GREETINGS_TASK_TEXT)

    def get_inbox(self):
        return self.api.get_tasks(project_id=self.api.get_project().id)


