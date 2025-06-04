import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckan.plugins import SingletonPlugin, implements
from ckan.plugins import IDatasetForm
from ckan.plugins.toolkit import get_action

import random
import logging

from ckan.plugins.toolkit import get_action

log = logging.getLogger(__name__)

# import ckanext.random.cli as cli
# import ckanext.random.helpers as helpers
# import ckanext.random.views as views
# from ckanext.random.logic import (
#     action, auth, validators
# )



class RandomPlugin(SingletonPlugin):
    implements(IDatasetForm, inherit=True)

    def before_create(self, context, data_dict):
        log.info("RandomNamePlugin: before_create triggered")

         # Remove existing name if provided
        data_dict.pop('name', None)

    # Generate a unique 5-digit number
        existing = get_action('package_show')
        while True:
            random_name = str(random.randint(10000, 99999))
            try:
                existing(context, {'id': random_name})
            except Exception:
                break

        data_dict['name'] = random_name
        log.info(f"RandomNamePlugin: assigned name {random_name}")
        return data_dict

    
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

