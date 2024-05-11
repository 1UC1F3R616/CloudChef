import json
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
    resources = [0] * num_resources
    task_completion = {}

    def find_earliest_resource(required_start):
        earliest_time = float('inf')
        index = 0
        for i in range(num_resources):
            if resources[i] <= required_start and resources[i] < earliest_time:
                earliest_time = resources[i]
                index = i
        return index

    for task in task_order:
        required_start = max((task_completion.get(dep, 0) for dep in tasks[task]['dependencies']), default=0)
        resource_index = find_earliest_resource(required_start)
        
        start_time = max(resources[resource_index], required_start)
        end_time = start_time + tasks[task]['timeRequired']
        
        resources[resource_index] = end_time
        task_completion[task] = end_time
    
    return max(resources)

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
