import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def randomnameplugin_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "randomnameplugin_get_sum": randomnameplugin_get_sum,
    }
