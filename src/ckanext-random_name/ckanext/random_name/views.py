from flask import Blueprint


random_name = Blueprint(
    "random_name", __name__)


def page():
    return "Hello, random_name!"


random_name.add_url_rule(
    "/random_name/page", view_func=page)


def get_blueprints():
    return [random_name]
