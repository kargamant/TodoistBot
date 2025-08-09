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

    def get_today(self):
        t_list = [t for t in self.api.filter_tasks(query='today', lang='ru')]
        return t_list[0]

    def get_inbox(self):
        return [task.content for task in self.api.get_tasks(project_id=self.api.get_projects()[0].id)]

    def get_categories(self):
        return [project.name for project in self.api.get_projects()[1::]]
