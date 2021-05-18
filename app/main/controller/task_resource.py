import json
from flask import jsonify, make_response, request
from flask_jwt import jwt_required
from flask_restx import Resource, api
from app.main.services.task_service import TaskService
from ..util import ResourceDto

api = ResourceDto.task_api

task_service = TaskService()


@api.route("task")
class Task_resource(Resource):

    @jwt_required()
    def post(self):
        data = json.loads(request.data.decode())
        id = task_service.create_task(data)
        return make_response(jsonify({"id": id}))

    def delete(self):
        data = json.loads(request.data.decode())
        task_service.delete_task(data["id"])
        return make_response("Task deleted successfully")
