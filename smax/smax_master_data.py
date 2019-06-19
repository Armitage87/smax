import urllib.parse
import requests
import json
from smax.smax_auth_wrapper import SmaxTenant


class MasterData(SmaxTenant):
    def __init__(self, base_url, user_name, password, tenant_id):
        super().__init__(base_url, user_name, password, tenant_id)

    def get_people(self, query_params, filters=None):
        """
        Get list of people based on params provided
        :param query_params: FieldIDs you want to query, encased in quotes, comma separated
        :param filters: Filters you'd like to apply, comma separated and encased in quotes, default is None
        :return: Returns JSON result of people
        """
        assert type(query_params) == str, 'Query params must be in string form'
        query_params = str(query_params).replace(' ', '')
        if filters:
            assert type(filters) == str, 'Filter params must be in string form'
            filters = SmaxTenant.fix_url_encode(urllib.parse.quote_plus(filters))
            query_endpoint = requests.get('{}/rest/{}/ems/Person/?layout={}&filters={}'
                                          .format(self.base_url, self.tenant_id, query_params, filters),
                                          cookies=self.get_cookie()).json()
            return query_endpoint
        query_endpoint = requests.get('{}/rest/{}/ems/Person/?layout={}'
                                      .format(self.base_url, self.tenant_id, query_params),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_person_by_id(self, person_id, fields_to_display):
        """
        Get person by ID
        :param person_id: ID of person
        :param fields_to_display: fields to return on query
        :return: Person details in JSON format
        """
        assert type(fields_to_display) == str, 'Fields must be in string format'
        fields_to_display.replace(' ', '')
        query = requests.get('{}/rest/{}/ems/Person/{}?layout={}'.format(self.base_url,
                                                                         self.tenant_id,
                                                                         person_id,
                                                                         fields_to_display),
                             cookies=self.get_cookie()).json()
        return query

    def get_groups(self, query_params, filters=None):
        """
        Get list of groups based on params provided
        :param query_params: FieldIDs you want to query, encased in quotes, comma separated
        :param filters: Filters you'd like to apply, comma separated and encased in quotes, default is None
        :return: Returns JSON result of groups
        """
        assert type(query_params) == str, 'Query params must be in string form'
        query_params = str(query_params).replace(' ', '')
        if filters:
            assert type(filters) == str, 'Filter params must be in string form'
            filters = SmaxTenant.fix_url_encode(urllib.parse.quote_plus(filters))
            query_endpoint = requests.get('{}/rest/{}/ems/PersonGroup/?layout={}&filters={}'
                                          .format(self.base_url, self.tenant_id, query_params, filters),
                                          cookies=self.get_cookie()).json()
            return query_endpoint
        query_endpoint = requests.get('{}/rest/{}/ems/PersonGroup/?layout={}'
                                      .format(self.base_url, self.tenant_id, query_params),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_group_by_id(self, group_id, fields_to_display):
        """
        Get group by ID
        :param group_id: ID of group
        :param fields_to_display: fields to display
        :return: Group details in JSON format
        """
        assert type(fields_to_display) == str, 'Fields must be in string format'
        fields_to_display.replace(' ', '')
        query = requests.get('{}/rest/{}/ems/PersonGroup/{}?layout={}'.format(self.base_url,
                                                                              self.tenant_id,
                                                                              group_id,
                                                                              fields_to_display),
                             cookies=self.get_cookie()).json()
        return query

    def get_locations(self, query_params, filters=None):
        """
        Get list of groups based on params provided
        :param query_params: FieldIDs you want to query, encased in quotes, comma separated
        :param filters: Filters you'd like to apply, comma separated and encased in quotes, default is None
        :return: Returns JSON result of groups
        """
        assert type(query_params) == str, 'Query params must be in string form'
        query_params = str(query_params).replace(' ', '')
        if filters:
            assert type(filters) == str, 'Filter params must be in string form'
            filters = SmaxTenant.fix_url_encode(urllib.parse.quote_plus(filters))
            query_endpoint = requests.get('{}/rest/{}/ems/Location/?layout={}&filters={}'
                                          .format(self.base_url, self.tenant_id, query_params, filters),
                                          cookies=self.get_cookie()).json()
            return query_endpoint
        query_endpoint = requests.get('{}/rest/{}/ems/Location/?layout={}'
                                      .format(self.base_url, self.tenant_id, query_params),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_location_by_id(self, location_id):
        """
        Get location by ID
        :param location_id: ID of location
        :return: Location details in JSON format
        """
        query = requests.get('{}/rest/{}/entity-page/initializationData/Location/{}'.format(self.base_url,
                                                                                            self.tenant_id,
                                                                                            location_id),
                             cookies=self.get_cookie()).json()
        return query

    def get_categories(self):
        """
        Get a list of categories
        :return: List of categories
        """
        query = requests.get('{}/rest/{}/ems/ITProcessRecordCategory?filter=(Level1ParentId+%3D+null)&layout=Level2'
                             'Parent,PhaseId,IsDeleted,DataDomains,Level1Parent,IsActive,ExplicitStakeholders,Name,'
                             'DisplayLabel,AllStakeholders,Lifetime,Expire,Level1ParentId,LastUpdateTime,'
                             'EmsCreationTime,Level2ParentId,Id,'
                             'ProcessId&order=DisplayLabel+asc&size=1000'.format(self.base_url,
                                                                                 self.tenant_id),
                             cookies=self.get_cookie()).json()
        return query

    def create_entity(self, entity_type, entity_payload):
        """
        Create entity, options are: Person
                                    PersonGroup
                                    Location
        :param entity_type: Define entity type to create
        :param entity_payload: Payload of create request
        :return: Result of create operation, ID of created entity, details of created entity
        """
        assert type(entity_payload) == dict, 'Payload must be a dict'
        assert (entity_type == 'Person' or entity_type == 'PersonGroup' or entity_type == 'Location'), \
            'entity type must be one of the following:\nPerson, PersonGroup, Location'
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
        Update entity, options are: Person
                                    PersonGroup
                                    Location
        :param entity_id: entity ID of entity to update
        :param entity_type: Define entity type to update
        :param entity_payload: Payload of update request
        :return: Result of update operation, ID of updated entity, details of updated entity
        """
        assert type(entity_payload) == dict, 'Payload must be a dict'
        assert type(entity_id) == int, 'entity ID must be an integer'
        assert (entity_type == 'Person' or entity_type == 'PersonGroup' or entity_type == 'Location'), \
            'entity type must be one of the following:\nPerson, PersonGroup, Location'
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
