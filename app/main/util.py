from flask_restx import Namespace, fields



class UserDto:
    api = Namespace('user', description='user related operations')
    # user = api.model('user', {
    #     'email': fields.String(required=True, description='user email address'),
    #     'username': fields.String(required=True, description='user username'),
    #     'password': fields.String(required=True, description='user password'),
    #     'public_id': fields.String(description='user Identifier')
    # })
    
class ResourceDto:
    task_api = Namespace('Resource', description='Task related operations')
    section_api = Namespace('Resource', description='Section related operations')
    label_api = Namespace('Resource', description='Label related operations')
    labels = label_api.model("Labels", {
    'id' : fields.Integer,
    'name' : fields.String,
    'color' : fields.String,
    'default' : fields.boolean,
    'shared' : {
        'primary' : fields.boolean,
         'users' : [{
            'user_id' : fields.Integer,
            'primary' : fields.boolean,
        }]    
    }
})
