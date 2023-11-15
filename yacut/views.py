from flask import flash, redirect, render_template

from . import Config, app, db
from .forms import LinkForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route("/", methods=["GET", "POST"])
def index_view():
    form = LinkForm()
    if not form.validate_on_submit():
        return render_template("form.html", form=form)
    short = form.custom_id.data or get_unique_short_id()
    if URLMap.query.filter_by(short=short).first() is not None:
        flash(
            "Предложенный вариант короткой ссылки уже существует.",
            "exists",
        )
    else:
        url = URLMap(original=form.original_link.data, short=short)
        db.session.add(url)
        db.session.commit()
        flash(f"{Config.BASE_LINK}{url.short}", "commit")
    return render_template("form.html", form=form)


@app.route("/<slug>/", methods=["GET"])
@app.route("/<slug>", methods=["GET"])
def redirect_short_link(slug):
    url = URLMap.query.filter_by(short=slug).first_or_404()
    return redirect(url.original)
