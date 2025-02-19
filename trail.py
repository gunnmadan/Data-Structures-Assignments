import heapq

class TaskManager:
    def __init__(self):
        self.task_heap = []
        self.task_finder = {}
        self.counter = 0

    def add_task(self, task_name, priority_level):
        # Remove any old entry, if exists
        if task_name in self.task_finder:
            self._remove_task(task_name)
        
        # Use counter to avoid conflict when tasks have the same priority
        entry = (priority_level, self.counter, task_name)
        self.task_finder[task_name] = entry
        heapq.heappush(self.task_heap, entry)
        self.counter += 1

    def get_most_urgent_task(self):
        while self.task_heap:
            priority, count, task_name = self.task_heap[0]
            if task_name != '<removed>':
                return task_name
            heapq.heappop(self.task_heap)
        return None

    def finish_most_urgent_task(self):
        while self.task_heap:
            priority, count, task_name = heapq.heappop(self.task_heap)
            if task_name != '<removed>':
                del self.task_finder[task_name]
                return task_name
        return None

    def get_next_n_tasks(self, n):
        return [task_name for _, _, task_name in heapq.nsmallest(n, self.task_heap)]

    def get_last_n_tasks(self, n):
        return [task_name for _, _, task_name in heapq.nlargest(n, self.task_heap)]

    def change_priority(self, task_name, new_priority):
        if task_name in self.task_finder:
            self._remove_task(task_name)
            self.add_task(task_name, new_priority)

    def _remove_task(self, task_name):
        entry = self.task_finder.pop(task_name)
        new_entry = (entry[0], entry[1], '<removed>')
        self.task_finder[task_name] = new_entry

# Driver code to test the TaskManager
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Task1", 2)
    manager.add_task("Task2", 1)
    manager.add_task("Task3", 3)

    print("Most urgent task:", manager.get_most_urgent_task())
    print("Finished urgent task:", manager.finish_most_urgent_task())
    print("Most urgent task:", manager.get_most_urgent_task())

    manager.add_task("Task4", 0)
    manager.change_priority("Task3", 0)

    print("Next 2 tasks:", manager.get_next_n_tasks(2))
    print("Last 2 tasks:", manager.get_last_n_tasks(2))
    print("Finished urgent task:", manager.finish_most_urgent_task())
    print("Next most urgent task:", manager.get_most_urgent_task())
