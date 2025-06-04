import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def random_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "random_get_sum": random_get_sum,
    }
