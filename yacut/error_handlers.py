from http import HTTPStatus

from flask import jsonify, render_template

from . import app, db


class InvalidAPIUsage(Exception):
    status_code = HTTPStatus.BAD_REQUEST

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return dict(message=self.message)


@app.errorhandler(404)
def handle_404_error(error):
    return render_template("404.html"), HTTPStatus.NOT_FOUND


@app.errorhandler(500)
def handle_internal_error(error):
    db.session.rollback()
    return render_template("500.html"), HTTPStatus.INTERNAL_SERVER_ERROR


@app.errorhandler(InvalidAPIUsage)
def handle_invalid_api_usage(error):
    db.session.rollback()
    return jsonify(error.to_dict()), error.status_code
