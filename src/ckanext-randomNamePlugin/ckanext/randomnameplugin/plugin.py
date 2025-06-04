import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import random
from ckan.plugins.toolkit import get_action, config

import logging
log = logging.getLogger(__name__)

# import ckanext.randomnameplugin.cli as cli
# import ckanext.randomnameplugin.helpers as helpers
# import ckanext.randomnameplugin.views as views
# from ckanext.randomnameplugin.logic import (
#     action, auth, validators
# )


class RandomnamepluginPlugin(plugins.SingletonPlugin):
    #plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IDatasetForm, inherit=True)
    
    # plugins.implements(plugins.IAuthFunctions)
    # plugins.implements(plugins.IActions)
    # plugins.implements(plugins.IBlueprint)
    # plugins.implements(plugins.IClick)
    # plugins.implements(plugins.ITemplateHelpers)
    # plugins.implements(plugins.IValidators)
    

    # IConfigurer
    
    def create_package_schema(self):
        schema = super(RandomnamepluginPlugin, self).create_package_schema()
        return schema
    def before_create(self, context, data_dict):
        log.error("RandomNamePlugin: before_create triggered")
        # Generate a random 5-digit number
        random_name = str(random.randint(10000, 99999))
   
        # Ensure uniqueness
        existing = get_action('package_show')
        while True:
            try:
                existing(context, {'id': random_name})
                random_name = str(random.randint(10000, 99999))
            except:
                break
        data_dict['name'] = random_name
        return data_dict
     

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "randomnameplugin")

    
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

    # def get_helpers(self):
    #     return helpers.get_helpers()

    # IValidators

    # def get_validators(self):
    #     return validators.get_validators()
    
