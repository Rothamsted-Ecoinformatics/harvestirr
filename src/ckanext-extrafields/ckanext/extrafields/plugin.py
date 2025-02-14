import ckan.plugins as plugins
import ckan.plugins.toolkit as tk
from ckan.types import Schema



class ExampleIDatasetFormPlugin(plugins.SingletonPlugin, tk.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IDatasetForm) 


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
            'journal': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'publisher': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'journal_volume': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'journal_issue': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'journal_page_range': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'isbn': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'issn': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'placeOf_publication': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'exiting_doi': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'pubMedID': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'webAddress': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'relatedOutput': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'openAccess': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'funder_code': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'funder_name': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'output_status': [tk.get_validator('ignore_missing'),
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
            'journal': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'publisher': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'journal_volume': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'journal_issue': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'journal_page_range': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'isbn': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'issn': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'placeOf_publication': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'exiting_doi': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'pubMedID': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'webAddress': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'relatedOutput': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'openAccess': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'funder_code': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'funder_name': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'output_status': [tk.get_validator('ignore_missing'),
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
            'journal': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'publisher': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'journal_volume': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'journal_issue': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'journal_page_range': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'isbn': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'issn': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'placeOf_publication': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'exiting_doi': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'pubMedID': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'webAddress': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'relatedOutput': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'openAccess': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'funder_code': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'funder_name': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'output_status': [tk.get_converter('convert_from_extras'),
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
            'journal': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'publisher': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'journal_volume': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'journal_issue': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'journal_page_range': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'isbn': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'issn': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'placeOf_publication': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'exiting_doi': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'pubMedID': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'webAddress': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'relatedOutput': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'openAccess': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'funder_code': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'funder_name': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'output_status': [tk.get_converter('convert_from_extras'),
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


    
