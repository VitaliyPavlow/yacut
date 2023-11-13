from . import app, db
from flask import jsonify, request
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import get_unique_short_id


@app.route("/api/id/", methods=["POST"])
@app.route("/api/id", methods=["POST"])
def add_short_link():
    data = request.get_json(silent=True)
    if data is None:
        raise InvalidAPIUsage("Отсутствует тело запроса")
    if "url" not in data:
        raise InvalidAPIUsage("'url' является обязательным полем!")
    url = URLMap()
    if "custom_id" not in data:
        url.short = get_unique_short_id()
    else:
        if len(custom_id := data["custom_id"]) > 16:
            raise InvalidAPIUsage(
                "Указано недопустимое имя для короткой ссылки"
            )
        if URLMap.query.filter_by(short=custom_id).first() is not None:
            raise InvalidAPIUsage(
                "Предложенный вариант короткой ссылки уже существует."
            )
        url.short = custom_id
    url.original = data["url"]
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), 201


@app.route("/api/id/<slug>/", methods=["GET"])
@app.route("/api/id/<slug>", methods=["GET"])
def get_original_link(slug):
    return slug
