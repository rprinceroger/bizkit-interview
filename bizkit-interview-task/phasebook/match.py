import time
from flask import Blueprint

from .data.match_data import MATCHES

bp = Blueprint("match", __name__, url_prefix="/match")

@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    is_match_result = is_match(MATCHES[match_id])
    end = time.time()

    message = "Match found" if is_match_result else "No match"
    return {"message": message, "elapsedTime": end - start}, 200

def is_match(match_data):
    fave_numbers_1, fave_numbers_2 = match_data
    set_fave_numbers_1 = set(fave_numbers_1)
    set_fave_numbers_2 = set(fave_numbers_2)

    return set_fave_numbers_2.issubset(set_fave_numbers_1)
