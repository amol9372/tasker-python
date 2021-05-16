from sqlalchemy.orm import backref
from app.main import db
from app.main.db_models.base_model import BaseModel


class Section(BaseModel):

    __tablename__ = "sections"

    name = db.Column(db.Text)
    # One to many with Tasks
    tasks = db.relationship("Task", backref="section", lazy="dynamic", cascade="all,delete")
    # Foreign key user_label_id
    label_id = db.Column(db.Integer, db.ForeignKey("labels.id"))

    def __init__(self, name, label_id):
        self.name = name
        self.label_id = label_id

    def create_section(section):
        db.session.add(section)
        db.session.flush()
        return section.id

    def get_sections(label_id):
        return Section.query.filter_by(label_id = label_id).all()

    def delete_section(id):
        section = Section.query.filter_by(id = id).first()
        db.session.delete(section)         

    def __repr__(self) -> str:
        if self.tasks:
            return "Section with name ::: {} and tasks ::: {}".format(self.name, self.tasks)
        else:
            return "Section with name ::: {}".format(self.name)
