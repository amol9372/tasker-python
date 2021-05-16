from app.main.business_models.base_buisness_model import BaseModel


class AppTask(BaseModel):

    def __init__(self, id, name, description, priority, status, schedule=""):
        super().__init__(id)
        self.name = name
        self.description = description
        self.priority = priority
        self.status = status
        self.schedule = schedule
