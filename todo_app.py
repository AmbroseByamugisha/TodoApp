class Todo:
    def __init__(self, name, created_at):
        self.name = name
        self.created_at = created_at

    def add_task(self, name):
        self.name = name
        return self.name

    def show_tasks(self, name):
        self.name = name
        return self.name

    def delete_task(self, name):
        self.name = name
        return self.name


class HomeTodo(Todo):
    def __init__(self, name, created_at, category):
        self.name = name
        self.created_at = created_at
        self.category = category

    def show_single_task(self, task_id):
        self.task_id
        return task_id
