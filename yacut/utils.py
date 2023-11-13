import random
import re
import string

from .models import URLMap


def get_unique_short_id() -> str:
    characters = string.ascii_letters + string.digits
    short = "".join(random.choices(characters, k=6))
    while URLMap.query.filter_by(short=short).first() is not None:
        short = get_unique_short_id()
    return short


def validation_custom_id(custom_id):
    return not re.search(r"[^A-Za-z0-9]", custom_id) and len(custom_id) <= 16
