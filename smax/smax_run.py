import json
import urllib.parse
import requests
from smax.smax_auth_wrapper import SmaxTenant


class Run(SmaxTenant):
    def __init__(self, base_url, user_name, password, tenant_id):
        super().__init__(base_url, user_name, password, tenant_id)

    def get_incidents(self, query_params, filters=None):
        """
        Get incidents based on params passed
        :param query_params: FieldIDs you want to query, encased in quotes, comma separated
        :param filters: Filters you'd like to apply, comma separated and encased in quotes, default is None
        :return: Returns JSON result of incident query
        """
        assert type(query_params) == str, 'Query params must be in string form'
        query_params = str(query_params).replace(' ', '')
        if filters:
            assert type(filters) == str, 'Filter params must be in string form'
            filters = SmaxTenant.fix_url_encode(urllib.parse.quote_plus(filters))
            query_endpoint = requests.get('{}/rest/{}/ems/Incident?layout={}&filter={}'
                                          .format(self.base_url, self.tenant_id, query_params, filters),
                                          cookies=self.get_cookie()).json()
            return query_endpoint
        query_endpoint = requests.get('{}/rest/{}/ems/Incident?layout={}'
                                      .format(self.base_url, self.tenant_id, query_params),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_incident_by_id(self, incident_id):
        """
        Get incident details by ID
        :param incident_id: ID of incident to query
        :return: Returns JSON result of incident query
        """
        query_endpoint = requests.get('{}/rest/{}/entity-page/initializationData/Incident/{}'
                                      .format(self.base_url, self.tenant_id, incident_id),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_incident_templates(self):
        """
        Returns the list of all incident templates
        :return: JSON of all incident templates
        """
        query_endpoint = requests.get('{}/rest/{}/rms/EntityTemplate?filter=(EntityType+%3D+%27Incident%27)'
                                      .format(self.base_url, self.tenant_id),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_incident_model_by_id(self, incident_model_id):
        """
        Get incident model by ID
        :param incident_model_id: ID of incident model to query
        :return: Returns JSON result of incident model query
        """
        query_endpoint = requests.get('{}/rest/{}/entity-page/initializationData/EntityModel/{}'
                                      .format(self.base_url, self.tenant_id, incident_model_id),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_incident_models(self, query_params, filters=None):
        """
        Get incident models based on params passed
        :param query_params: FieldIDs you want to query, encased in quotes, comma separated
        :param filters: Filters you'd like to apply, comma separated and encased in quotes, default is None
        :return: Returns JSON result of incident models query
        """
        assert type(query_params) == str, 'Query params must be in string form'
        query_params = str(query_params).replace(' ', '')
        if filters:
            assert type(filters) == str, 'Filter params must be in string form'
            filters = SmaxTenant.fix_url_encode(urllib.parse.quote_plus(filters))
            query_endpoint = requests.get('{}/rest/{}/ems/EntityModel?layout={}&filter={}'
                                          .format(self.base_url, self.tenant_id, query_params, filters),
                                          cookies=self.get_cookie()).json()
            return query_endpoint
        query_endpoint = requests.get('{}/rest/{}/ems/EntityModel?layout={}'
                                      .format(self.base_url, self.tenant_id, query_params),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_problems(self, query_params, filters=None):
        """
        Get problems based on params passed
        :param query_params: FieldIDs you want to query, encased in quotes, comma separated
        :param filters: Filters you'd like to apply, comma separated and encased in quotes, default is None
        :return: Returns JSON result of problem query
        """
        assert type(query_params) == str, 'Query params must be in string form'
        query_params = str(query_params).replace(' ', '')
        if filters:
            assert type(filters) == str, 'Filter params must be in string form'
            filters = SmaxTenant.fix_url_encode(urllib.parse.quote_plus(filters))
            query_endpoint = requests.get('{}/rest/{}/ems/Problem?layout={}&filter={}'
                                          .format(self.base_url, self.tenant_id, query_params, filters),
                                          cookies=self.get_cookie()).json()
            return query_endpoint
        query_endpoint = requests.get('{}/rest/{}/ems/Problem?layout={}'
                                      .format(self.base_url, self.tenant_id, query_params),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_problem_by_id(self, problem_id):
        """
        Get problem details by ID
        :param problem_id: ID of problem to query
        :return: Returns JSON result of problem query
        """
        query_endpoint = requests.get('{}/rest/{}/entity-page/initializationData/Problem/{}'
                                      .format(self.base_url, self.tenant_id, problem_id),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_service_requests(self, query_params, filters=None):
        """
        Get service requests based on params passed
        :param query_params: FieldIDs you want to query, encased in quotes, comma separated
        :param filters: Filters you'd like to apply, comma separated and encased in quotes, default is None
        :return: Returns JSON result of service request query
        """
        assert type(query_params) == str, 'Query params must be in string form'
        query_params = str(query_params).replace(' ', '')
        if filters:
            assert type(filters) == str, 'Filter params must be in string form'
            filters = SmaxTenant.fix_url_encode(urllib.parse.quote_plus(filters))
            query_endpoint = requests.get('{}/rest/{}/ems/Request?layout={}&filter={}'
                                          .format(self.base_url, self.tenant_id, query_params, filters),
                                          cookies=self.get_cookie()).json()
            return query_endpoint
        query_endpoint = requests.get('{}/rest/{}/ems/Request?layout={}'
                                      .format(self.base_url, self.tenant_id, query_params),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_service_request_by_id(self, request_id):
        """
        Get service request details by ID
        :param request_id: ID of service request to query
        :return: Returns JSON result of service request query
        """
        query_endpoint = requests.get('{}/rest/{}/entity-page/initializationData/Request/{}'
                                      .format(self.base_url, self.tenant_id, request_id),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_licenses(self, query_params, filters=None):
        """
        Get licences based on params passed
        :param query_params: FieldIDs you want to query, encased in quotes, comma separated
        :param filters: Filters you'd like to apply, comma separated and encased in quotes, default is None
        :return: Returns JSON result of software asset licences query
        """
        assert type(query_params) == str, 'Query params must be in string form'
        query_params = str(query_params).replace(' ', '')
        if filters:
            assert type(filters) == str, 'Filter params must be in string form'
            filters = SmaxTenant.fix_url_encode(urllib.parse.quote_plus(filters))
            query_endpoint = requests.get('{}/rest/{}/ems/License?layout={}&filter={}'
                                          .format(self.base_url, self.tenant_id, query_params, filters),
                                          cookies=self.get_cookie()).json()
            return query_endpoint
        query_endpoint = requests.get('{}/rest/{}/ems/License?layout={}'
                                      .format(self.base_url, self.tenant_id, query_params),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_license_by_id(self, licence_id):
        """
        Get licences from software assets section
        :param licence_id: Licence ID
        :return: Returns JSON result of software assets licence query
        """
        query_endpoint = requests.get('{}/rest/{}/entity-page/initializationData/License/{}'
                                      .format(self.base_url, self.tenant_id, licence_id),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_license_type_by_id(self, licence_type_id):
        """
        Get licence type from software assets section
        :param licence_type_id: Licence type ID
        :return: Returns JSON result of software assets licence type query
        """
        query_endpoint = requests.get('{}/rest/{}/entity-page/initializationData/LicenseType/{}'
                                      .format(self.base_url, self.tenant_id, licence_type_id),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_license_types(self, query_params, filters=None):
        """
        Get licence types based on params passed
        :param query_params: FieldIDs you want to query, encased in quotes, comma separated
        :param filters: Filters you'd like to apply, comma separated and encased in quotes, default is None
        :return: Returns JSON result of software asset licence types query
        """
        assert type(query_params) == str, 'Query params must be in string form'
        query_params = str(query_params).replace(' ', '')
        if filters:
            assert type(filters) == str, 'Filter params must be in string form'
            filters = SmaxTenant.fix_url_encode(urllib.parse.quote_plus(filters))
            query_endpoint = requests.get('{}/rest/{}/ems/LicenseType?layout={}&filter={}'
                                          .format(self.base_url, self.tenant_id, query_params, filters),
                                          cookies=self.get_cookie()).json()
            return query_endpoint
        query_endpoint = requests.get('{}/rest/{}/ems/LicenseType?layout={}'
                                      .format(self.base_url, self.tenant_id, query_params),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_license_model_by_id(self, licence_model_id):
        """
        Get licence model from software assets section
        :param licence_model_id: Licence model ID
        :return: Returns JSON result of software assets licence model query
        """
        query_endpoint = requests.get('{}/rest/{}/entity-page/initializationData/AssetModel/{}'
                                      .format(self.base_url, self.tenant_id, licence_model_id),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_license_models(self, query_params, filters=None):
        """
        Get licence models based on params passed
        :param query_params: FieldIDs you want to query, encased in quotes, comma separated
        :param filters: Filters you'd like to apply, comma separated and encased in quotes, default is None
        :return: Returns JSON result of licence models query
        """
        assert type(query_params) == str, 'Query params must be in string form'
        query_params = str(query_params).replace(' ', '')
        if filters:
            assert type(filters) == str, 'Filter params must be in string form'
            filters = SmaxTenant.fix_url_encode(urllib.parse.quote_plus(filters))
            query_endpoint = requests.get('{}/rest/{}/ems/AssetModel?layout={}&filter={}'
                                          .format(self.base_url, self.tenant_id, query_params, filters),
                                          cookies=self.get_cookie()).json()
            return query_endpoint
        query_endpoint = requests.get('{}/rest/{}/ems/AssetModel?layout={}'
                                      .format(self.base_url, self.tenant_id, query_params),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_software_title_by_id(self, software_title_id):
        """
        Get software title from software assets section
        :param software_title_id: Software title ID
        :return: Returns JSON result of software assets software title query
        """
        query_endpoint = requests.get('{}/rest/{}/entity-page/initializationData/AssetModel/{}'
                                      .format(self.base_url, self.tenant_id, software_title_id),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_software_titles(self, query_params, filters=None):
        """
        Get software titles based on params passed
        :param query_params: FieldIDs you want to query, encased in quotes, comma separated
        :param filters: Filters you'd like to apply, comma separated and encased in quotes, default is None
        :return: Returns JSON result of software assets software titles query
        """
        assert type(query_params) == str, 'Query params must be in string form'
        query_params = str(query_params).replace(' ', '')
        if filters:
            assert type(filters) == str, 'Filter params must be in string form'
            filters = SmaxTenant.fix_url_encode(urllib.parse.quote_plus(filters))
            query_endpoint = requests.get('{}/rest/{}/ems/AssetModel?layout={}&filter={}'
                                          .format(self.base_url, self.tenant_id, query_params, filters),
                                          cookies=self.get_cookie()).json()
            return query_endpoint
        query_endpoint = requests.get('{}/rest/{}/ems/AssetModel?layout={}'
                                      .format(self.base_url, self.tenant_id, query_params),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_fixed_asset_by_id(self, asset_id):
        """
        Get fixed asset by ID
        :param asset_id: Fixed asset ID
        :return: Returns JSON result of fixed asset query
        """
        query_endpoint = requests.get('{}/rest/{}/entity-page/initializationData/FixedAsset/{}'
                                      .format(self.base_url, self.tenant_id, asset_id),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_fixed_assets(self, query_params, filters=None):
        """
        Get fixed assets based on params passed
        :param query_params: FieldIDs you want to query, encased in quotes, comma separated
        :param filters: Filters you'd like to apply, comma separated and encased in quotes, default is None
        :return: Returns JSON result of fixed assets query
        """
        assert type(query_params) == str, 'Query params must be in string form'
        query_params = str(query_params).replace(' ', '')
        if filters:
            assert type(filters) == str, 'Filter params must be in string form'
            filters = SmaxTenant.fix_url_encode(urllib.parse.quote_plus(filters))
            query_endpoint = requests.get('{}/rest/{}/ems/FixedAsset/?layout={}&filter={}'
                                          .format(self.base_url, self.tenant_id, query_params, filters),
                                          cookies=self.get_cookie()).json()
            return query_endpoint
        query_endpoint = requests.get('{}/rest/{}/ems/FixedAsset/?layout={}'
                                      .format(self.base_url, self.tenant_id, query_params),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def create_entity(self, entity_type, entity_payload):
        """
        Create entity, options are: Incident
                                    Problem
                                    License
                                    LicenseType
                                    Request
                                    AssetModel
                                    FixedAsset
        :param entity_type: Define entity type to create
        :param entity_payload: Payload of create request
        :return: Result of create operation, ID of created entity, details of created entity
        """
        assert type(entity_payload) == dict, 'Payload must be a dict'
        assert (entity_type == 'Incident' or entity_type == 'Problem' or entity_type == 'License' or
                entity_type == 'LicenseType' or entity_type == 'Request' or entity_type == 'AssetModel' or
                entity_type == 'FixedAsset'), \
            'entity type must be one of the following:\nIncident, Problem, License, LicenseType, ' \
            'Request, AssetModel, FixedAsset'
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
        Update entity, options are: Incident
                                    Problem
                                    License
                                    LicenseType
                                    Request
                                    AssetModel
                                    FixedAsset
        :param entity_id: entity ID of entity to update
        :param entity_type: Define entity type to update
        :param entity_payload: Payload of update request
        :return: Result of update operation, ID of updated entity, details of updated entity
        """
        assert type(entity_payload) == dict, 'Payload must be a dict'
        assert type(entity_id) == int, 'entity ID must be an integer'
        assert (entity_type == 'Incident' or entity_type == 'Problem' or entity_type == 'License' or
                entity_type == 'LicenseType' or entity_type == 'Request' or entity_type == 'AssetModel' or
                entity_type == 'FixedAsset'), \
            'entity type must be one of the following:\nIncident, Problem, License, LicenseType, ' \
            'Request, AssetModel, FixedAsset'
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
