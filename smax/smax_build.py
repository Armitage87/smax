import json
import urllib.parse
import requests
from smax.smax_auth_wrapper import SmaxTenant


class Build(SmaxTenant):
    def __init__(self, base_url, user_name, password, tenant_id):
        super().__init__(base_url, user_name, password, tenant_id)

    def get_changes(self, query_params, filters=None):
        """
        Get changes based on params passed
        :param query_params: FieldIDs you want to query, encased in quotes, comma separated
        :param filters: Filters you'd like to apply, comma separated and encased in quotes, default is None
        :return: Returns JSON result of change query
        """
        assert type(query_params) == str, 'Query params must be in string form'
        query_params = str(query_params).replace(' ', '')
        if filters:
            assert type(filters) == str, 'Filter params must be in string form'
            filters = SmaxTenant.fix_url_encode(urllib.parse.quote_plus(filters))
            query_endpoint = requests.get('{}/rest/{}/ems/Change/?layout={}&filter={}'
                                          .format(self.base_url, self.tenant_id, query_params, filters),
                                          cookies=self.get_cookie()).json()
            return query_endpoint
        query_endpoint = requests.get('{}/rest/{}/ems/Change/?layout={}'
                                      .format(self.base_url, self.tenant_id, query_params),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_change_by_id(self, change_id):
        """
        Get change details by ID
        :param change_id: ID of change to query
        :return: Returns JSON result of change query
        """
        query_endpoint = requests.get('{}/rest/{}/entity-page/initializationData/Change/{}'
                                      .format(self.base_url, self.tenant_id, change_id),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_change_form(self):
        """
        Gets change form, showing all available fields and data types in them
        :return: JSON result of change form
        """
        query = requests.get('{}/rest/{}/forms/Change'.format(self.base_url, self.tenant_id),
                             cookies=self.get_cookie()).json()
        return query

    def get_change_templates(self):
        """
        Returns the list of all change templates
        :return: JSON of all change templates
        """
        query_endpoint = requests.get('{}/rest/{}/rms/EntityTemplate?filter=(EntityType+%3D+%27Change%27)'
                                      .format(self.base_url, self.tenant_id),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_change_model_by_id(self, change_model_id):
        """
        Get change model by ID
        :param change_model_id: ID of change model
        :return: Change model details in JSON format
        """
        query = requests.get('{}/rest/{}/entity-page/initializationData/EntityModel/{}'.format(self.base_url,
                                                                                               self.tenant_id,
                                                                                               change_model_id),
                             cookies=self.get_cookie()).json()
        return query

    def get_releases(self, query_params, filters=None):
        """
        Get releases based on params passed
        :param query_params: FieldIDs you want to query, encased in quotes, comma separated
        :param filters: Filters you'd like to apply, comma separated and encased in quotes, default is None
        :return: Returns JSON result of release query
        """
        assert type(query_params) == str, 'Query params must be in string form'
        query_params = str(query_params).replace(' ', '')
        if filters:
            assert type(filters) == str, 'Filter params must be in string form'
            filters = SmaxTenant.fix_url_encode(urllib.parse.quote_plus(filters))
            query_endpoint = requests.get('{}/rest/{}/ems/Release/?layout={}&filter={}'
                                          .format(self.base_url, self.tenant_id, query_params, filters),
                                          cookies=self.get_cookie()).json()
            return query_endpoint
        query_endpoint = requests.get('{}/rest/{}/ems/Release/?layout={}'
                                      .format(self.base_url, self.tenant_id, query_params),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_release_by_id(self, release_id):
        """
        Get release by ID
        :param release_id: ID of release
        :return: Release details in JSON format
        """
        query = requests.get('{}/rest/{}/entity-page/initializationData/Release/{}'.format(self.base_url,
                                                                                           self.tenant_id,
                                                                                           release_id),
                             cookies=self.get_cookie()).json()
        return query

    def get_release_model_by_id(self, release_model_id):
        """
        Get release model by ID
        :param release_model_id: ID of change model
        :return: Release model details in JSON format
        """
        query = requests.get('{}/rest/{}/entity-page/initializationData/EntityModel/{}'.format(self.base_url,
                                                                                               self.tenant_id,
                                                                                               release_model_id),
                             cookies=self.get_cookie()).json()
        return query

    def get_article_form(self):
        """
        Gets article form with all fields and data types
        :return: JSON result of article form
        """
        query = requests.get('{}/rest/{}/forms/Article'.format(self.base_url, self.tenant_id),
                             cookies=self.get_cookie()).json()
        return query

    def get_knowledge_articles(self, query_params, filters=None):
        """
        Get knowledge articles on params passed
        :param query_params: FieldIDs you want to query, encased in quotes, comma separated
        :param filters: Filters you'd like to apply, comma separated and encased in quotes, default is None
        :return: Returns JSON result of knowledge articles
        """
        assert type(query_params) == str, 'Query params must be in string form'
        query_params = str(query_params).replace(' ', '')
        if filters:
            assert type(filters) == str, 'Filter params must be in string form'
            filters = SmaxTenant.fix_url_encode(urllib.parse.quote_plus(filters))
            query_endpoint = requests.get('{}/rest/{}/ems/Article/?layout={}&filter={}'
                                          .format(self.base_url, self.tenant_id, query_params, filters),
                                          cookies=self.get_cookie()).json()
            return query_endpoint
        query_endpoint = requests.get('{}/rest/{}/ems/Article/?layout={}'
                                      .format(self.base_url, self.tenant_id, query_params),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_knowledge_article_by_id(self, article_id, parse_html=False):
        """
        Get knowledge article by ID, set parse_html to True if you
        want to parse HTML content of knowledge article
        :param article_id: ID of article
        :param parse_html: Set to true to parse HTML output of article
        :return: Knowledge base article details in JSON format
        """

        query = requests.get('{}/rest/{}/entity-page/initializationData/Article/{}'.format(self.base_url,
                                                                                           self.tenant_id,
                                                                                           article_id),
                             cookies=self.get_cookie()).json()
        if parse_html:
            for k, v in query.items():
                new_value = SmaxTenant.parse_output(str(v))
                query[k] = new_value
            return query
        return query

    def get_knowledge_model_by_id(self, knowledge_model_id):
        """
        Get knowledge model by ID
        :param knowledge_model_id: ID of change model
        :return: Knowledge model details in JSON format
        """
        query = requests.get('{}/rest/{}/entity-page/initializationData/EntityModel/{}'.format(self.base_url,
                                                                                               self.tenant_id,
                                                                                               knowledge_model_id),
                             cookies=self.get_cookie()).json()
        return query

    def get_service_definitions(self, query_params, filters=None):
        """
        Get service definitions on params passed
        :param query_params: FieldIDs you want to query, encased in quotes, comma separated
        :param filters: Filters you'd like to apply, comma separated and encased in quotes, default is None
        :return: Returns JSON result of service definitions
        """
        assert type(query_params) == str, 'Query params must be in string form'
        query_params = str(query_params).replace(' ', '')
        if filters:
            assert type(filters) == str, 'Filter params must be in string form'
            filters = SmaxTenant.fix_url_encode(urllib.parse.quote_plus(filters))
            query_endpoint = requests.get('{}/rest/{}/ems/ServiceDefinition/?layout={}&filter={}'
                                          .format(self.base_url, self.tenant_id, query_params, filters),
                                          cookies=self.get_cookie()).json()
            return query_endpoint
        query_endpoint = requests.get('{}/rest/{}/ems/ServiceDefinition/?layout={}'
                                      .format(self.base_url, self.tenant_id, query_params),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_service_definition_by_id(self, service_definition_id):
        """
        Get service definition by ID
        :param service_definition_id: ID of service definition
        :return: Servie definition details in JSON format
        """
        query = requests.get('{}/rest/{}/entity-page/initializationData/ServiceDefinition/{}'.format(self.base_url,
                                                                                                     self.tenant_id,
                                                                                                     service_definition_id),
                             cookies=self.get_cookie()).json()
        return query

    def get_service_definition_form(self):
        """
        Gets service definition form with all fields and data types
        :return: JSON result of all fields in service definition form
        """
        query = requests.get('{}/rest/{}/forms/ServiceDefinition'.format(self.base_url, self.tenant_id),
                             cookies=self.get_cookie()).json()
        return query

    def get_actual_services(self, query_params, filters=None):
        """
        Get actual services on params passed
        :param query_params: FieldIDs you want to query, encased in quotes, comma separated
        :param filters: Filters you'd like to apply, comma separated and encased in quotes, default is None
        :return: Returns JSON result of actual services
        """
        assert type(query_params) == str, 'Query params must be in string form'
        query_params = str(query_params).replace(' ', '')
        if filters:
            assert type(filters) == str, 'Filter params must be in string form'
            filters = SmaxTenant.fix_url_encode(urllib.parse.quote_plus(filters))
            query_endpoint = requests.get('{}/rest/{}/ems/ActualService/?layout={}&filter={}'
                                          .format(self.base_url, self.tenant_id, query_params, filters),
                                          cookies=self.get_cookie()).json()
            return query_endpoint
        query_endpoint = requests.get('{}/rest/{}/ems/ActualService/?layout={}'
                                      .format(self.base_url, self.tenant_id, query_params),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_actual_service_by_id(self, actual_service_id):
        """
        Get actual service by ID
        :param actual_service_id: ID of actual service
        :return: Actual service details in JSON format
        """
        query = requests.get('{}/rest/{}/entity-page/initializationData/ActualService/{}'.format(self.base_url,
                                                                                                 self.tenant_id,
                                                                                                 actual_service_id),
                             cookies=self.get_cookie()).json()
        return query

    def get_actual_services_form(self):
        """
        Gets actual services form with all fields and data types
        :return: JSON result of actual service form
        """
        query = requests.get('{}/rest/{}/forms/ActualService'.format(self.base_url, self.tenant_id),
                             cookies=self.get_cookie()).json()
        return query

    def create_entity(self, entity_type, entity_payload):
        """
        Create entity, options are: Change
                                    Release
                                    EntityModel
                                    Article
                                    ServiceDefinition
                                    ActualService
        :param entity_type: Define entity type to create
        :param entity_payload: Payload of create request
        :return: Result of create operation, ID of created entity, details of created entity
        """
        assert type(entity_payload) == dict, 'Payload must be a dict'
        assert (entity_type == 'Change' or entity_type == 'Release' or entity_type == 'EntityModel' or
                entity_type == 'Article' or entity_type == 'ServiceDefinition' or entity_type == 'ActualService'), \
            'entity type must be one of the following:\nChange, Release, EntityModel, Article, ' \
            'ServiceDefinition, ActualService'
        header = self.headers
        base_payload = {"entities": [{
            "entity_type": "{}".format(entity_type),
            "properties": {}
        }
        ],
            "operation": "CREATE"
        }
        base_payload['entities'][0]['properties'] = entity_payload
        entity_creation_payload = json.dumps(base_payload)
        entity_creation = requests.post('{}/rest/{}/ems/bulk'.format(self.base_url, self.tenant_id),
                                        cookies=self.get_cookie(), data=entity_creation_payload,
                                        headers=header).json()
        return entity_creation

    def update_entity(self, entity_id, entity_type, entity_payload):
        """
        Update entity, options are: Change
                                    Release
                                    EntityModel
                                    Article
                                    ServiceDefinition
                                    ActualService
        :param entity_id: entity ID of entity to update
        :param entity_type: Define entity type to update
        :param entity_payload: Payload of update request
        :return: Result of update operation, ID of updated entity, details of updated entity
        """
        assert type(entity_payload) == dict, 'Payload must be a dict'
        assert type(entity_id) == int, 'entity ID must be an integer'
        assert (entity_type == 'Change' or entity_type == 'Release' or entity_type == 'EntityModel' or
                entity_type == 'Article' or entity_type == 'ServiceDefinition' or entity_type == 'ActualService'), \
            'entity type must be one of the following:\nChange, Release, EntityModel, Article, ' \
            'ServiceDefinition, ActualService'
        header = self.headers
        base_payload = {"entities": [{
            "entity_type": "{}".format(entity_type),
            "properties": {}
        }
        ],
            "operation": "UPDATE"
        }
        base_payload['entities'][0]['properties'] = {'Id': entity_id}
        base_payload['entities'][0]['properties'].update(entity_payload)
        entity_update_payload = json.dumps(base_payload)
        entity_update = requests.post('{}/rest/{}/ems/bulk'.format(self.base_url, self.tenant_id),
                                      cookies=self.get_cookie(), data=entity_update_payload,
                                      headers=header).json()
        return entity_update


