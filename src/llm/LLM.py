from llama_cpp import Llama, LLAMA_SPLIT_MODE_NONE
from llm_config import MODEL_PATH, CATEGORIZE_INBOX_PROMPT, EXTRACT_CATEGORIES_PROMPT
import os

class LLM:
    def __init__(self):
        self.llm = Llama(
            model_path=os.path.join(os.path.dirname(__file__), MODEL_PATH),
            n_gpu_layers=-1,
            split_mode=LLAMA_SPLIT_MODE_NONE,
            n_threads=12
        )



    def sort_inbox(self, tasks: list, categories: list):
        task_str = ',\n'.join(tasks)
        categories_str = ',\n'.join(categories)

        response = self.llm.create_chat_completion(
            messages=[
                {
                    'role' : 'system',
                    'content' : CATEGORIZE_INBOX_PROMPT
                },
                {
                    'role' : 'user',
                    'content' : f'This is a list of my tasks in inbox: {task_str}.\n '
                                f'And here is a list of categories {categories_str}.\n'
                }
            ]
        )
        self.llm.reset()
        return response['choices'][0]['message']['content']

    def extract_inbox_categories(self, message: str):
        response = self.llm.create_chat_completion(
            messages=[
                {
                    'role': 'system',
                    'content': EXTRACT_CATEGORIES_PROMPT
                },
                {
                    'role': 'user',
                    'content': message
                }
            ]
        )
        self.llm.reset()
        return response['choices'][0]['message']['content']

llm = LLM()
response = llm.extract_inbox_categories(llm.sort_inbox(['open new bank account at Tinkoff bank',
                                                        'buy milk',
                                                        'find a job',
                                                        'start going to the gym'],
                                                       ['personal', 'career', 'finances', 'daily']))
print(response)
# Example json response
# {
#   "tasks": [
#     {
#       "task": "Open new bank account at Tinkoff Bank",
#       "category": "finances"
#     },
#     {
#       "task": "Buy milk",
#       "category": "daily"
#     },
#     {
#       "task": "Find a job",
#       "category": "career"
#     },
#     {
#       "task": "Start going to the gym",
#       "category": "personal"
#     }
#   ]
# }