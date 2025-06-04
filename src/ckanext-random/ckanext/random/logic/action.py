import ckan.plugins.toolkit as tk
import ckanext.random.logic.schema as schema


@tk.side_effect_free
def random_get_sum(context, data_dict):
    tk.check_access(
        "random_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.random_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'random_get_sum': random_get_sum,
    }
