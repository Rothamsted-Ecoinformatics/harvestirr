from flask import Blueprint


random = Blueprint(
    "random", __name__)


def page():
    return "Hello, random!"


random.add_url_rule(
    "/random/page", view_func=page)


def get_blueprints():
    return [random]
