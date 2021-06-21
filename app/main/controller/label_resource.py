import json
from flask import jsonify, make_response, request
from flask_jwt import jwt_required, current_identity
from flask_restx import Resource, api, fields
from app.main.business_models.label import Label
from app.main.db_models.task.label_detail import LabelDetail
from ..util import ResourceDto
from ..services.label_service import LabelService
from app.main.services import label_service

api = ResourceDto.label_api

labels = ResourceDto.labels

label_service = LabelService()


@api.route("label")
class Labels(Resource):

    @jwt_required()
    def post(self):
        data = json.loads(request.data.decode())
        user_id = current_identity.__dict__["id"]
        label_id = label_service.create_label(data, user_id)
        return make_response(jsonify({"id": label_id}), 200)

    # @api.expect(labels, validate = False)

    @jwt_required()
    def get(self):
        # data = json.loads(request.data.decode())
        user_id = current_identity.__dict__["id"]
        user_labels = label_service.get_labels(user_id=user_id)
        return user_labels

    def delete(self):
        data = json.loads(request.data.decode())
        label_service.delete_label(data['id'])
        return make_response("Label deleted successfully")
