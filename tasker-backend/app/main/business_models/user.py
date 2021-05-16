from app.main.business_models.base_buisness_model import BaseModel


class AppUser(BaseModel):

    def __init__(self, id, name, email):
        super().__init__(id)
        self.name = name
        self.email = email