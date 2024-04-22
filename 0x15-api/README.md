## 0x15. API

# Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
Libraries imported in your Python files must be organized in alphabetical order
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
You must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
Your code should not be executed when imported (by using if __name__ == "__main__":)

# # 1. Export to CSV

Using what you did in the task #0, extend your Python script to export data in the CSV format.

Requirements:

Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv

# 2. Export to JSONUsing what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
File name must be: USER_ID.json

# 3. Dictionary of list of dictionaries
Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

Records all tasks from all employees
Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
File name must be: todo_all_employees.json 
