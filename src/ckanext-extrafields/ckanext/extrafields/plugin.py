import ckan.plugins as plugins
import ckan.plugins.toolkit as tk
from ckan.types import Schema

# import ckanext.extrafields.cli as cli
# import ckanext.extrafields.helpers as helpers
# import ckanext.extrafields.views as views
# from ckanext.extrafields.logic import (
#     action, auth, validators
# )


class ExampleIDatasetFormPlugin(plugins.SingletonPlugin, tk.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IDatasetForm) 
    # plugins.implements(plugins.IAuthFunctions)
    # plugins.implements(plugins.IActions)
    # plugins.implements(plugins.IBlueprint)
    # plugins.implements(plugins.IClick)
    # plugins.implements(plugins.ITemplateHelpers)
    # plugins.implements(plugins.IValidators)
    

    # IConfigurer

    def update_config(self, config_):
        tk.add_template_directory(config_, "templates")
        tk.add_public_directory(config_, "public")
        tk.add_resource("assets", "extrafields")
   
    def create_package_schema(self) -> Schema:
        # let's grab the default schema in our plugin
        schema: Schema = super(
            ExampleIDatasetFormPlugin, self).create_package_schema()
        # our custom field
        schema.update({
            'publication_type': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'publication_year': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'contributor_name': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'contributor_email': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'contributor_type': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
        })
        return schema
    def update_package_schema(self) -> Schema:
        schema: Schema = super(
            ExampleIDatasetFormPlugin, self).update_package_schema()
        # our custom field
        schema.update({
            'publication_type': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'publication_year': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'contributor_name': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'contributor_email': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'contributor_type': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
        })
        return schema
    def show_package_schema(self) -> Schema:
        schema: Schema = super(
            ExampleIDatasetFormPlugin, self).show_package_schema()
        schema.update({
            'publication_type': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'publication_year': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'contributor_name': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'contributor_email': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'contributor_type': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
        })
        return schema
        schema: Schema = super(
            ExampleIDatasetFormPlugin, self).show_package_schema()
        schema.update({
            'publication_type': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'publication_year': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'contributor_name': [tk.get_converter('convert_from_extras'), 
                            tk.get_validator('ignore_missing')],
            'contributor_email': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'contributor_type': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
        })
        return schema

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self) -> list[str]:
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []
    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')


    
