from copy import copy
from flask import Blueprint, jsonify, request
from repos.area_repo import AreaRepo
from models.area import Area


def construct_area_blueprint(database):
    area_blueprint = Blueprint(__name__, 'area', url_prefix='/areas')

    area_repo = AreaRepo(database)

    @area_blueprint.route('/', methods=['GET'])
    def get_areas():
        return jsonify([area.toFullDict() for area in area_repo.get_areas()])

    @area_blueprint.route('/<areaID>', methods=['PATCH'])
    def patch_area(areaID):
        assert(request.headers['Content-Type'] == 'application/json')
        updatedArea = request.json
        f = Area().toFullDict()
        g = copy(f)
        for k in f:
            if k in updatedArea:
                g[k] = updatedArea[k]
        print("updating ", areaID, " to ", g)
        area_repo.patch_area(areaID, Area(**g))
        return "Success"

    return area_blueprint
