import random
import string
from ckan.plugins import implements, SingletonPlugin, IDatasetForm
from ckan.plugins import toolkit

class RandomDatasetNamePlugin(SingletonPlugin):
    implements(IDatasetForm, inherit=True)

    def _generate_random_name(self):
        return 'dataset-' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

    def create_package_schema(self):
        schema = toolkit.default_create_package_schema()

        def random_name(key, data, errors, context):
            if not data.get('name'):
                data['name'] = self._generate_random_name()

        schema['name'] = [random_name] + schema['name']
        return schema

    def update_package_schema(self):
        return toolkit.default_update_package_schema()

    def is_fallback(self):
        return True  # Optional, only if needed
