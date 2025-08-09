MODEL_PATH = 'qwen2-0_5b-instruct-q5_k_m.gguf'

# prompts
CATEGORIZE_INBOX_PROMPT = 'You are great at categorizing tasks by categories. ' \
                    'You will be given a list of different tasks from user inbox bin and a list of categories. ' \
                    'DO NOT GIVE ANY COMMENTS ON TASKS THEMSELVES. DO NOT GIVE ANY COMMENTS ABOUT CATEGORIES.' \
                    'Your task is to send a list of tasks with categories they are suitable to be in.' \
                    'For example:' \
                    'task_1 - category_1' \
                    'task_2 - category_2' \
                    '...'
EXTRACT_CATEGORIES_PROMPT = 'YOU SHOULD NOT GIVE ANY COMMENTS ABOUT CONTENTS OF PROMPT.' \
                            'You will be given a message containing a list of tasks and categories.' \
                            'DONT WRITE ANY EXTRA COMMENTS. Just extract them and give them in json format.' \
