from copy import copy
from flask import Blueprint, jsonify, request, abort
from repos.area_repo import AreaRepo
from models.area import Area


def construct_area_blueprint(database):
    area_blueprint = Blueprint(__name__, 'area', url_prefix='/areas')

    area_repo = AreaRepo(database)

    @area_blueprint.route('/', methods=['GET'])
    def get_areas():
        return jsonify([area.toFullDict() for area in area_repo.get_areas()])

    @area_blueprint.route('/<area_id>', methods=['GET'])
    def get_area_by_id(area_id):
        area = area_repo.get_area_by_id(area_id)
        if area is None:
            abort(404)
        else:
            return jsonify(area.toFullDict())

    @area_blueprint.route('/<area_id>', methods=['PATCH'])
    def patch_area(area_id):
        assert(request.headers['Content-Type'] == 'application/json')
        updated_area = request.json
        f = Area().toFullDict()
        g = copy(f)
        for k in f:
            if k in updated_area:
                g[k] = updated_area[k]
        print("updating ", area_id, " to ", g)
        area_repo.patch_area(area_id, Area(**g))
        return jsonify({"message":"Success"})

    return area_blueprint
