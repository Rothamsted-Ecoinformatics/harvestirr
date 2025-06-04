import ckan.plugins.toolkit as tk
import ckanext.randomnameplugin.logic.schema as schema


@tk.side_effect_free
def randomnameplugin_get_sum(context, data_dict):
    tk.check_access(
        "randomnameplugin_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.randomnameplugin_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'randomnameplugin_get_sum': randomnameplugin_get_sum,
    }
