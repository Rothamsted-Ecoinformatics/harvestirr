import ckan.plugins.toolkit as tk


def random_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "random_required": random_required,
    }
