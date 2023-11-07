from flask_wtf import FlaskForm
from wtforms import URLField, StringField, SubmitField
from wtforms.validators import Length, Optional, URL, Regexp


class LinkForm(FlaskForm):
    original_link = URLField(
        "Укорочаемая ссылка",
        validators=[Length(1, 256), URL(message="Неправильный URL")]
    )
    custom_id = StringField(
        "Кастомное имя",
        validators=[
            Length(1, 16),
            Regexp(regex=r"^[A-Za-z0-9]+$", message="Неправильное имя"),
            Optional()
        ]
    )
    submit = SubmitField("Создать")