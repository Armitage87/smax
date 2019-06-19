import requests
from smax.smax_auth_wrapper import SmaxTenant


class Configuration(SmaxTenant):
    def __init__(self, base_url, user_name, password, tenant_id):
        super().__init__(base_url, user_name, password, tenant_id)

    def get_records_fields(self, entity_type):
        """
        Get all fields for specific entity type
        :param entity_type: Entity type of fields to query
        :return: JSON output of all fields for specified entity
        """
        query_endpoint = requests.get('{}/rest/{}/metadata/ui/entity-descriptors/{}'
                                      .format(self.base_url, self.tenant_id, entity_type),
                                      cookies=self.get_cookie()).json()
        return query_endpoint

    def get_workflows(self, entity_type):
        """
        Get workflow configuration of entity specified
        :param entity_type: Type of entity to query
        :return: JSON configuration of workflows
        """
        query_endpoint = requests.get('{}/rest/{}/workflow/full/{}'
                                      .format(self.base_url, self.tenant_id, entity_type),
                                      cookies=self.get_cookie()).json()
        return query_endpoint
