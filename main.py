class Task:

    def __init__(self, description, deadline, status="не выполнено"):

        self.description = description
        self.deadline = deadline
        self.status = status


class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):

        self.tasks.append(task)

    def current_tasks_list(self):

        current_tasks = [task for task in self.tasks if task.status == "не выполнено"]
        for i, task in enumerate(current_tasks):
            print(f"Задача {i + 1}: {task.description}, до {task.deadline}")

    def mark_task_as_done(self, task_index):
        self.tasks[task_index].status = "выполнено"


task1 = Task("Подготовить отчет", "15.10.2024")
task2 = Task("Сделать презентацию", "20.10.2024")
task3 = Task("Отправить документы", "25.10.2024")

task_manager = TaskManager()
task_manager.add_task(task1)
task_manager.add_task(task2)
task_manager.add_task(task3)

task_manager.mark_task_as_done(1)

task_manager.current_tasks_list()
