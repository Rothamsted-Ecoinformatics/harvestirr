import random
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.model import Package

class RandomDatasetNamePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IPlugin)  # basic plugin interface

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'random_name')

    def before_create(self, context, data_dict):
        if not data_dict.get('name'):
            data_dict['name'] = self._generate_unique_random_name()
        return data_dict

    def before_update(self, context, data_dict):
        # Prevent changing name on edit
        if 'name' in data_dict:
            del data_dict['name']
        return data_dict

    def _generate_unique_random_name(self):
        while True:
            candidate = str(random.randint(10000, 99999))
            if not Package.get(candidate):
                return candidate
