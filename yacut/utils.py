import string
import random


def get_unique_short_id() -> str:
    characters = string.ascii_letters + string.digits
    return "".join(random.choices(characters, k=6))
