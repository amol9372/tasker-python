from app.main import db
from app.main.db_models.base_model import BaseModel


class Task(BaseModel):

    __tablename__ = "tasks"

    name = db.Column(db.Text)
    description = db.Column(db.Text)
    # Foreign key column
    section_id = db.Column(db.Integer, db.ForeignKey("sections.id"))
    priority = db.Column(db.Text)
    completed = db.Column(db.Boolean)
    scheduled = db.Column(db.Text)

    def __init__(self, name, section_id, priority, description=None, scheduled=None, completed=False):
        self.name = name
        self.description = description
        self.section_id = section_id
        self.completed = completed
        self.priority = priority
        self.scheduled = scheduled

    def create_task(task):
        db.session.add(task)
        db.session.flush()
        return task.id

    def get_tasks_for_section(section_id):
        return Task.query.filter_by(section_id=section_id).all()

    def delete_task(id):
        Task.query.filter_by(id=id).delete()

    def __repr__(self) -> str:
        return "Task with name ::: {} and section ::: {} and status ::: {}".format(self.name, self.section_id, self.completed)
