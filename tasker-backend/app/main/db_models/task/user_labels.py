from app.main.db_models.base_model import BaseModel
from app.main import db


class UserLabels(BaseModel):

    __tablename__ = "user_labels"

    label_id = db.Column(db.Integer, db.ForeignKey("labels.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    primary_user = db.Column(db.Boolean)
    default = db.Column(db.Boolean)
    user = db.relationship("User", backref="UserLabels", uselist=False)

    def __init__(self, label_id, user_id, primary_user, default=False):
        self.user_id = user_id
        self.label_id = label_id
        self.primary_user = primary_user
        self.default = default

    def get_user_labels(user_id):
        return UserLabels.query.filter_by(user_id=user_id).all()

    def create_user_label(user_label):
        db.session.add(user_label)
        db.session.flush()
        return user_label.id

    def get_user_labels_by_label_id(label_id):
        return UserLabels.query.filter_by(label_id=label_id).all()

    def delele_user_label(user_label):
        db.session.delete(user_label)
        db.session.flush()

    def __repr__(self) -> str:
        return "Shared Label with label_id ::: {} and user_id ::: {} and primary user ::: {}".format(self.label_id, self.user_id, self.primary_user)
