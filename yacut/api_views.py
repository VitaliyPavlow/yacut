from . import app, db
from flask import jsonify, request
from .error_handlers import InvalidAPIUsage
from .models import URLMap


@app.route("/api/id/", methods=["POST"])
def add_short_link():
    data = request.get_json(silent=True)
    if data is None:
        raise InvalidAPIUsage("Вы отправили пустой запрос :(")
    if 'url' not in data:
        raise InvalidAPIUsage('В запросе отсутствуют обязательные поля')
    url = URLMap()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), 201


@app.route("/api/id/<slug>/", methods=["GET"])
def get_original_link(slug):
    return slug