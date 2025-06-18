import random
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.model import Package

class RandomDatasetNamePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IResourceUrlChange)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IDatasetForm)

    def update_config(self, config):
        # Add our template and static files
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'random_name')

    def get_helpers(self):
        return {
            'generate_random_dataset_name': self.generate_random_dataset_name
        }

    def generate_random_dataset_name(self):
        """Helper to be used in template to generate a unique random name."""
        while True:
            candidate = str(random.randint(10000, 99999))
            if not Package.get(candidate):
                return candidate

    def before_create(self, context, data_dict):
        # Set name only if not provided (i.e., during form load)
        if not data_dict.get('name'):
            data_dict['name'] = self.generate_random_dataset_name()
        return data_dict

    def before_update(self, context, data_dict):
        # Do not change the name if already set
        if 'name' in data_dict:
            del data_dict['name']
        return data_dict
