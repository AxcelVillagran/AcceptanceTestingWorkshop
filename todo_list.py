from task import Task

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.task_id_counter = 1

    def add_task(self, title, description):
        task = Task(self.task_id_counter, title, description)
        self.tasks.append(task)
        self.task_id_counter += 1

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for task in self.tasks:
                print(task)

    def mark_task_completed(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_completed()
                return True
        return False

    def mark_task_pending(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_pending()
                return False
        return True


    def clear_tasks(self):
        self.tasks.clear()
