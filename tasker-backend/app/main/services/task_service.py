from app.main import transaction
from app.main.db_models.task.tasks import Task


class TaskService():

    def __init__(self) -> None:
        pass

    @transaction()
    def create_task(self, data):
        task = Task(name=data["name"], priority=data["priority"],
                    section_id=data["section_id"], completed=False)
        return Task.create_task(task)

    @transaction()
    def delete_task(self, id):
        Task.delete_task(id)
