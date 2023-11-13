from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import get_unique_short_id, validation_custom_id


@app.route("/api/id/", methods=["POST"])
@app.route("/api/id", methods=["POST"])
def add_short_link():
    data = request.get_json(silent=True)
    if data is None:
        raise InvalidAPIUsage("Отсутствует тело запроса")
    if "url" not in data:
        raise InvalidAPIUsage("\"url\" является обязательным полем!")
    url = URLMap()
    if (
        "custom_id" not in data
        or data["custom_id"] is None
        or data["custom_id"] == ""
    ):
        url.short = get_unique_short_id()
    else:
        if not validation_custom_id(custom_id := data["custom_id"]):
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
    try:
        original = URLMap.query.filter_by(short=slug).first().original
        return {"url": original}
    except AttributeError:
        raise InvalidAPIUsage("Указанный id не найден", status_code=404)
