from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, Length, Optional, Regexp


class LinkForm(FlaskForm):
    original_link = URLField(
        "Укорачаемая ссылка",
        validators=[Length(1, 256), URL(message="Неправильный URL")],
    )
    custom_id = StringField(
        "Кастомное имя",
        validators=[
            Length(1, 16),
            Regexp(regex=r"^[A-Za-z0-9]+$", message="Неправильное имя"),
            Optional(),
        ],
    )
    submit = SubmitField("Создать")
