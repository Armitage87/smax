import json
import requests


class SmaxAdmin(object):
    def __init__(self, base_url, user_name, password, account_id):
        """
        Initiate main wrapper class and connection details
        :param base_url: Base url of your SMAX instance
        :param user_name: user name of admin user
        :param password: password of admin user
        :param account_id: Suite ID of your instance
        """
        self.base_url = base_url
        self.user_name = user_name
        self.password = password
        self.account_id = str(account_id)
        self.headers = {'Content-Type': 'application/json'}

    @staticmethod
    def get_help(function):
        """
        Get help with specific function
        :param function: function to display help for
        :return: Help doc for requested function
        """
        return function.__doc__

    def get_admin_cookie(self):
        """
        Authenticate calls against authentication endpoint
        :return: cookie to pass with each subsequent request
        """
        SMAX_AUTH = '{}/auth/authentication-endpoint/authenticate/login?ACCOUNTID={}'. \
            format(self.base_url, self.account_id)
        payload = {'Login': '{}'.format(self.user_name), 'Password': '{}'.format(self.password)}
        payload = json.dumps(payload)
        smax_token = requests.post(SMAX_AUTH, data=payload)
        auth_c = str(smax_token.content.decode("utf-8"))
        cookie_smax = {'LWSSO_COOKIE_KEY': '{0}'.format(auth_c)}
        return cookie_smax

    def get_users(self):
        """
        Get a list of users
        :return: list of users in json format
        """
        query_endpoint = requests.get('{}/bo/rest/entities/user'
                                      .format(self.base_url),
                                      cookies=self.get_admin_cookie()).json()
        return query_endpoint

    def get_user_by_id(self, user_id):
        """
        Get specific details of user
        :param user_id: ID of user to query
        :return: User details in JSON format
        """
        query_endpoint = requests.get('{}/bo/rest/entities/user/{}'
                                      .format(self.base_url, user_id),
                                      cookies=self.get_admin_cookie()).json()
        return query_endpoint

    def attach_user_to_tenant(self, user_id, tenant_id):
        """
        Attach user to specified tenant
        :param user_id: ID of user to attach
        :param tenant_id: Tenant ID to attach to
        :return: Result of operation in JSON format
        """
        payload = {"tenantId": tenant_id,
                   "attachEntities":
                       [{"id": user_id, "entityType": "user"}]}
        payload_to_put = json.dumps(payload)
        attach_request = requests.put('{}/bo/rest/entities/user/attachOrRemove'.format(self.base_url),
                                      cookies=self.get_admin_cookie(), data=payload_to_put,
                                      headers=self.headers).json()
        return attach_request

    def get_accounts(self):
        """
        Get a list of accounts
        :return: list of accounts in json format
        """
        query_endpoint = requests.get('{}/bo/rest/entities/account'
                                      .format(self.base_url),
                                      cookies=self.get_admin_cookie()).json()
        return query_endpoint

    def get_customers(self):
        """
        Get a list of customers
        :return: list of customers in json format
        """
        query_endpoint = requests.get('{}/bo/rest/entities/customer'
                                      .format(self.base_url),
                                      cookies=self.get_admin_cookie()).json()
        return query_endpoint

    def get_tenants(self):
        """
        Get a list of tenants
        :return: list of tenants in json format
        """
        query_endpoint = requests.get('{}/bo/rest/entities/tenant'
                                      .format(self.base_url),
                                      cookies=self.get_admin_cookie()).json()
        return query_endpoint

    def get_tenant_by_id(self, tenant_id):
        """
        Get tenant details by ID
        :param tenant_id: ID of tenant to query
        :return: Tenant details in JSON format
        """
        query_endpoint = requests.get('{}/bo/rest/entities/tenant/{}'
                                      .format(self.base_url, tenant_id),
                                      cookies=self.get_admin_cookie()).json()
        return query_endpoint

    def change_tenant_settings(self, tenant_it, payload):
        """
        Change tenant settings, this is sensitive endpoint and best way to go about this is to
        query tenant you want to modify (using get_tenant_by_id), and take that payload and
        change setting you want then send it via this function
        :param tenant_it: ID of tenant you wish to change
        :param payload: Payload of items to change
        :return: Result of operation in JSON format
        """
        payload_to_put = json.dumps(payload)
        request_to_change = requests.put('{}/bo/rest/entities/tenant/{}'.format(self.base_url, tenant_it),
                                         cookies=self.get_admin_cookie(), data=payload_to_put,
                                         headers=self.headers).json()
        return request_to_change

    def delete_tenant(self, tenant_id):
        """
        This method will delete the tenant, bear in mind that this operation is not reversible, use with caution!
        :param tenant_id: ID of tenant to delete
        :return: Result of operation
        """
        payload = [{"id": tenant_id,
                    "entityType": "tenant"}]
        delete_payload = json.dumps(payload)
        delete_tenant = requests.delete('{}/bo/rest/entities/tenant'.format(self.base_url),
                                        cookies=self.get_admin_cookie(), data=delete_payload,
                                        headers=self.headers).json()
        return delete_tenant

    def get_license_pools(self):
        """
        Get a list of license pools
        :return: list of license pools in json format
        """
        query_endpoint = requests.get('{}/bo/rest/entities/licensePool'
                                      .format(self.base_url),
                                      cookies=self.get_admin_cookie()).json()
        return query_endpoint

    def get_licenses(self):
        """
        Get a list of licenses
        :return: list of licenses in json format
        """
        query_endpoint = requests.get('{}/bo/rest/entities/license'
                                      .format(self.base_url),
                                      cookies=self.get_admin_cookie()).json()
        return query_endpoint

    def get_license_activity(self):
        """
        Get a list of license activities
        :return: list of license activities in json format
        """
        query_endpoint = requests.get('{}/bo/rest/entities/licenseActivity'
                                      .format(self.base_url),
                                      cookies=self.get_admin_cookie()).json()
        return query_endpoint

    def get_configurations(self, config_section):
        """
        Get configurations
        :param config_section: Which configuration to review
        :return: Current configuration in JSON format
        """
        configs = {
            'security': 'lwsso',
            'email': 'smtp',
            'export': 'backup',
            'ldap': 'ldap',
            'index': 'idolIndex',
            'license': 'licenseNotification'
        }
        assert (config_section == 'security' or config_section == 'email' or config_section == 'export' or
                config_section == 'ldap' or config_section == 'index' or config_section == 'license'), \
            'Please select one of the following\nsecurity, email, export, ldap, index, license'
        config_section = str(config_section).lower()
        config_selection = configs.get(config_section, None)
        query_endpoint = requests.get('{}/bo/rest/entities/configurations/{}'.format(self.base_url, config_selection),
                                      cookies=self.get_admin_cookie()).json()
        return query_endpoint

    def get_operation_history(self):
        """
        Get operation history
        :return: Operation history in json format
        """
        query_endpoint = requests.get('{}/bo/rest/entities/operationHistory'
                                      .format(self.base_url),
                                      cookies=self.get_admin_cookie()).json()
        return query_endpoint

    def get_operation_history_by_id(self, operation_id):
        """
        Get specific details of operation
        :param operation_id: ID of operation to query
        :return: Operation details in JSON format
        """
        query_endpoint = requests.get('{}/bo/rest/entities/operationHistory/{}'
                                      .format(self.base_url, operation_id),
                                      cookies=self.get_admin_cookie()).json()
        return query_endpoint