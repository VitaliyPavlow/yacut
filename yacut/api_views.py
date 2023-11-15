from http import HTTPStatus

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import get_unique_short_id, validate_custom_id


@app.route("/api/id/", methods=["POST"])
def add_short_link():
    data = request.get_json(silent=True)
    if data is None:
        raise InvalidAPIUsage("Отсутствует тело запроса")
    if "url" not in data:
        raise InvalidAPIUsage("\"url\" является обязательным полем!")
    url = URLMap()
    if not data.get("custom_id"):
        url.short = get_unique_short_id()
    else:
        if not validate_custom_id(custom_id := data["custom_id"]):
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
    return jsonify(url.to_dict()), HTTPStatus.CREATED


@app.route("/api/id/<slug>/", methods=["GET"])
def get_original_link(slug):
    url_mapping = URLMap.query.filter_by(short=slug).first()
    if url_mapping:
        return {"url": url_mapping.original}
    raise InvalidAPIUsage(
        "Указанный id не найден", status_code=HTTPStatus.NOT_FOUND
    )
