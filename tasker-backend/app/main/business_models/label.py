from app.main.business_models.base_buisness_model import BaseModel


class Label(BaseModel):
    def __init__(self, id, name, color, default, shared=None, sections=0):
        super().__init__(id)
        self.name = name
        self.color = color
        self.default = default
        self.shared = shared
        self.sections = sections
