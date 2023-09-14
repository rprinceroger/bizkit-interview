from flask import Blueprint, request

from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")

@bp.route("")
def search():
    search_params = request.args.to_dict()
    search_results = search_users(search_params)
    sorted_results = sort_users(search_results)
    return {"users": sorted_results}, 200

def search_users(search_params):
    matching_users = []

    for user in USERS:
        if matches_criteria(user, search_params):
            matching_users.append(user)

    return matching_users

def matches_criteria(user, search_params):
    if not search_params:
        return True  # If no search parameters are provided, include all users

    if 'id' in search_params and search_params['id'] == user['id']:
        return True

    if 'name' in search_params and contains_partial_search(user['name'], search_params['name']):
        return True

    if 'age' in search_params and is_age_within_range(user['age'], search_params['age']):
        return True

    if 'occupation' in search_params and contains_partial_search(user['occupation'], search_params['occupation']):
        return True

    return False

def contains_partial_search(text, keyword):
    return keyword.lower() in text.lower()

def is_age_within_range(user_age, search_age):
    try:
        user_age = int(user_age)
        search_age = int(search_age)
        return abs(user_age - search_age) <= 1
    except ValueError:
        return False

def sort_users(users):
    return sorted(users, key=lambda user: (user['id'], user['name'], user['age'], user['occupation']))


