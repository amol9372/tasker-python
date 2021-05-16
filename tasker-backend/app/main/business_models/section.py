from app.main.business_models.base_buisness_model import BaseModel


class AppSection(BaseModel):

    def __init__(self,id, name, tasks=[]):
        super().__init__(id)
        self.name = name
        self.tasks = tasks
