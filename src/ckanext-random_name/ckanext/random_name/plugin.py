import random
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.model import Package


class RandomDatasetNamePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IDatasetForm)

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'random_name')

    def create_package_schema(self):
        schema = toolkit.default_create_package_schema()
        if 'name' in schema:
            del schema['name']  # remove to allow auto-generation
        return schema

    def update_package_schema(self):
        return toolkit.default_update_package_schema()

    def show_package_schema(self):
        return toolkit.default_show_package_schema()

    def before_create(self, context, data_dict):
        # Only generate name if it doesn't already exist
        if not data_dict.get('name'):
            data_dict['name'] = self._generate_unique_random_name()
        return data_dict

    def before_update(self, context, data_dict):
        # Prevent name from being changed during update
        if 'name' in data_dict:
            del data_dict['name']
        return data_dict

    def _generate_unique_random_name(self):
        while True:
            candidate = str(random.randint(10000, 99999))
            if not Package.get(candidate):
                return candidate
