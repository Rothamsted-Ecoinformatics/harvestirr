from flask import Blueprint


randomnameplugin = Blueprint(
    "randomnameplugin", __name__)


def page():
    return "Hello, randomnameplugin!"


randomnameplugin.add_url_rule(
    "/randomnameplugin/page", view_func=page)


def get_blueprints():
    return [randomnameplugin]
