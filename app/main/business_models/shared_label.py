from xmlrpc.client import Boolean

from app.main.business_models.base_buisness_model import BaseModel

class SharedLabel(BaseModel):

    def __init__(self, users, primary=False):
        self.primary = primary
        self.users = users # list of shared users for the label