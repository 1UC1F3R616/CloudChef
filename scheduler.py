import json
import heapq
from collections import defaultdict, deque

def topological_sort(tasks):
    in_degree = {task: 0 for task in tasks}
    graph = defaultdict(list)
    
    for task, attr in tasks.items():
        for dep in attr['dependencies']:
            graph[dep].append(task)
            in_degree[task] += 1
    
    queue = deque([t for t in in_degree if in_degree[t] == 0])
    sorted_tasks = []
    
    while queue:
        task = queue.popleft()
        sorted_tasks.append(task)
        for next_task in graph[task]:
            in_degree[next_task] -= 1
            if in_degree[next_task] == 0:
                queue.append(next_task)
    
    if len(sorted_tasks) != len(tasks):
        raise ValueError("There is a cycle in the dependencies.")
    
    return sorted_tasks

def schedule_tasks(tasks, num_resources):
    task_order = topological_sort(tasks)
    
    # Each element in the heap is a tuple (resource_end_time, resource_index)
    resource_heap = [(0, i) for i in range(num_resources)]
    heapq.heapify(resource_heap)
    
    task_completion = {}

    for task in task_order:
        required_start = max((task_completion.get(dep, 0) for dep in tasks[task]['dependencies']), default=0)
        
        # Pop the resource with the earliest available time
        earliest_end_time, resource_index = heapq.heappop(resource_heap)
        
        start_time = max(earliest_end_time, required_start)
        end_time = start_time + tasks[task]['timeRequired']
        
        # Push the updated resource back into the heap
        heapq.heappush(resource_heap, (end_time, resource_index))
        
        task_completion[task] = end_time
    
    # The total completion time is the max end time in the heap
    return max(end_time for end_time, _ in resource_heap)

def main():
    # Load task data from a JSON file
    with open('tasks.json', 'r') as f:
        tasks = json.load(f)
    
    # Number of resources available
    num_resources = 2

    # Schedule tasks and print the total completion time
    total_time = schedule_tasks(tasks, num_resources)
    print(f"Total completion time with {num_resources} resources is: {total_time}")

if __name__ == '__main__':
    main()
