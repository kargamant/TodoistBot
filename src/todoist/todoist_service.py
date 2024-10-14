import todoist_api_python.api as td
from .todoist_config import GREETINGS_TASK_TEXT
from requests.exceptions import HTTPError


async def verify_token(access_token: str) -> True | False:
    try:
        api = td.TodoistAPI(access_token)
        api.add_task(content=GREETINGS_TASK_TEXT)
    except HTTPError:
        return False
    return True


class TodoistService:
    def __init__(self, access_token: str):
        self.api = td.TodoistAPI(access_token)



#
# api = td.TodoistAPI('')
# print(api.get_projects())
#
# api.add_task(content='Hi from todoist ai helper', project_id='2299802935')