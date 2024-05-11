## Scheduling Strategy:
- Non-Preemptive Scheduling Using a Version of the Longest Processing Time (LPT) Algorithm:

- Implemented a non-preemptive scheduling strategy based on the LPT algorithm that assigns tasks to resources based on their durations, aimed at balancing workload and minimizing overall completion time.

- Dependency Management Through Topological Sorting: Tasks are sorted and scheduled using topological sorting to ensure that all dependencies are respected. Tasks are scheduled as soon as their prerequisites are completed and a resource becomes available.

## Scheduling Logic:
- Topological Sorting: Ensure tasks respect dependencies.
- Scheduling Using Min-Heap: Efficiently manage resource loads, assigning tasks to the least loaded resource as determined by a priority queue (min-heap) for optimal resource utilization.

![alt text](<img1.jpg>)

## Running the program
- Python needs to be installed
- Update the value of num_resources (n: available resources)
- `tasks.json` needs to be in same directory as of scheduling script
- run the the script: `python scheduler.py`

### Time Complexity:
- Sorting Tasks: The initial sorting of the tasks by their required times in descending order is done once. Assuming the number of tasks is  m, the sorting operation typically has a time complexity of: O(mlogm)
- Allocating Tasks to Resources: By maintaining a min-heap (or priority queue) where each entry is a resource with its current load. Inserting into a min-heap is O(logN), and doing this m times (once for each task): O(mlogN)
- Total: `O(mlogm+mlogN)`

## Visualization:
- I started with the idea of shifting code to js and have grpahical representation by marking nodes to show progress but because it was taking time so dropping that idea.
- Other idea is to open a socket connection with backend and frontend and show the live changes or give user option to move to next step and simply use api, for using api also changes are exhaustive to the backend code as need to maintain proper session state for a user.
- Option 3 is to simply use existing script and add some prints to showcase the progression.