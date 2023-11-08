import string
import random
from .models import URLMap


def get_unique_short_id() -> str:
    characters = string.ascii_letters + string.digits
    short = "".join(random.choices(characters, k=6))
    while URLMap.query.filter_by(short=short).first() is not None:
        short = get_unique_short_id()
    return short
