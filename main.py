class Task:
    def __init__(self, description, deadline, status=False):
        self.description = description
        self.deadline = deadline
        self.status = status

    def __str__(self):
        return f"{self.description}, Срок: {self.deadline}, Выполнена: {'Да' if self.status else 'Нет'}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        self.tasks.append(Task(description, deadline))

    def complete_task(self, description):
        for task in self.tasks:
            if task.description == description:
                task.status = True
                break

    def current_tasks(self):
        return [task for task in self.tasks if not task.status]

    def completed_tasks(self):
        return [task for task in self.tasks if task.status]

# Тестирование классов
task_manager = TaskManager()
task_manager.add_task("Закончить домашнее задание по Python", "26-03-2024")
task_manager.add_task("Выполнить дополнительное домашнее задание", "28-03-2024")
task_manager.complete_task("Закончить домашнее задание по Python")

# Вывод текущих задач
print("Текущие задачи:")
current_tasks = task_manager.current_tasks()
for task in current_tasks:
    print(task)

# Вывод выполненных задач
print("\nВыполненные задачи:")
completed_tasks = task_manager.completed_tasks()
for task in completed_tasks:
    print(task)
