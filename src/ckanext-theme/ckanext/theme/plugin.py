from ckan.common import CKANConfig
from pylons import config
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


# import ckanext.theme.cli as cli
# import ckanext.theme.helpers as helpers
# import ckanext.theme.views as views
# from ckanext.theme.logic import (
#     action, auth, validators
# )


class ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    
    # plugins.implements(plugins.IAuthFunctions)
    # plugins.implements(plugins.IActions)
    # plugins.implements(plugins.IBlueprint)
    # plugins.implements(plugins.IClick)
    plugins.implements(plugins.ITemplateHelpers)
    # plugins.implements(plugins.IValidators)
    

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        #toolkit.add_public_directory(config_, "public")
        #toolkit.add_resource("assets", "theme")

    
    # IAuthFunctions

    # def get_auth_functions(self):
    #     return auth.get_auth_functions()

    # IActions

    # def get_actions(self):
    #     return action.get_actions()

    # IBlueprint

    # def get_blueprint(self):
    #     return views.get_blueprints()

    # IClick

    # def get_commands(self):
    #     return cli.get_commands()

    # ITemplateHelpers

    def get_helpers(self):     
        return { 'my_custom_setting': self._get_my_custom_setting}

    def _get_my_custom_setting(self):
        return config.get('my.custom.setting', 'default_value')
    # IValidators

    # def get_validators(self):
    #     return validators.get_validators()
    
