## Schduling Strategy:
- Non Preemptive scheduling using a version of the Longest Processing Time (LPT) algorithm.
- Main idea here is to determine the Critical Path - the longest sequence of tasks that must be finished for all tasks to complete.
- This will be done in 3 steps:
    - Step 1: Topological Sorting
        - Order the tasks based on their dependencies. This can be achieved using a topological sort algorithm.

    - Step 2: Calculate Earliest Start Times
        - Once sorted, traverse the tasks from start to finish, calculating the earliest start time for each task based on the completion of its prerequisites.

    - Step 3: Calculate Latest Start Times
        - Traverse the tasks in reverse order (from finish to start) to determine the latest each task can start without delaying the project. This step helps identify the critical path by highlighting tasks with no slack.

![alt text](<img1.jpg>)

## Running the program
- Python needs to be installed
- Update the value of num_resources (n: available resources)
- `tasks.json` needs to be in same directory as of scheduling script
- run the the script: `python scheduler.py`

## Visualization:
- I started with the idea of shifting code to js and have grpahical representation by marking nodes to show progress but because it was taking time so dropping that idea.
- Other idea is to open a socket connection with backend and frontend and show the live changes or give user option to move to next step and simply use api, for using api also changes are exhaustive to the backend code as need to maintain proper session state for a user.
- Option 3 is to simply use existing script and add some prints to showcase the progression.