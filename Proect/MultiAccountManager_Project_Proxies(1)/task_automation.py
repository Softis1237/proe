
class TaskAutomation:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def run_tasks(self):
        results = []
        for task in self.tasks:
            try:
                result = task()
                results.append(f"Task succeeded: {result}")
            except Exception as e:
                results.append(f"Task failed: {e}")
        return results

# Example tasks
if __name__ == "__main__":
    automation = TaskAutomation()
    automation.add_task(lambda: "Task 1 completed")
    automation.add_task(lambda: "Task 2 completed")
    print(automation.run_tasks())
