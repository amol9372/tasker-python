from app.main import db
from app.main.db_models import user
from app.main.db_models.base_model import BaseModel

class LabelDetail(BaseModel):

    __tablename__ = "labels"
    
    name = db.Column(db.Text)
    # one to many
    sections = db.relationship("Section", backref="labeldetail", lazy="dynamic", cascade="all,delete")
    # foreign key user_id
    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # default = db.Column(db.Boolean)
    color = db.Column(db.Text)

    def __init__(self, name, color):
        self.name = name
        # self.user_id = user_id
        self.color = color

    # @staticmethod
    def create_label(label):
        db.session.add(label)
        db.session.flush()
        return label.id

    # @staticmethod
    def get_label(label_id) :
        return LabelDetail.query.filter_by(id=label_id).first()    

    def delete(id):
        label = LabelDetail.query.filter_by(id = id).first()
        db.session.delete(label)    