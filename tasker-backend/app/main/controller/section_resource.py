import json
from flask import jsonify, make_response, request
from flask_jwt import jwt_required
from flask_restx import Resource, api

from app.main.services.section_service import SectionService
from ..util import ResourceDto

api = ResourceDto.section_api

section_service = SectionService()


@api.route("section")
class Section_resource(Resource):

    @jwt_required()
    def post(self):
        data = json.loads(request.data.decode())
        id = section_service.create_section(data)
        return make_response(jsonify({"id": id}))

    @jwt_required()
    def get(self):
        label_id = int(request.args.get('label_id'))
        return section_service.get_all_sections(label_id)

    def delete(self):
        data = json.loads(request.data.decode())
        section_service.delete_section(data['id'])
        return make_response("Section deleted successfully")
