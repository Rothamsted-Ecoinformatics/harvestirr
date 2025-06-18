import ckan.plugins.toolkit as tk


def random_name_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "random_name_required": random_name_required,
    }
