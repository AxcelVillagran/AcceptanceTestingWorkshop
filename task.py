class Task:
    def __init__(self, task_id, title, description):
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def mark_pending(self):
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"[{self.id}] {self.title}: {self.description} - {status}"
