import json
import re
import requests


class SmaxTenant(object):
    def __init__(self, base_url, user_name, password, tenant_id):
        """
        Initiate main wrapper class and connection details
        :param base_url: Base url of your SMAX instance
        :param user_name: user name of user/integration user
        :param password: password of user/integration user
        :param tenant_id: tenant ID of your instance
        """
        self.base_url = base_url
        self.user_name = user_name
        self.password = password
        self.tenant_id = str(tenant_id)
        self.headers = {'Content-Type': 'application/json'}

    def get_cookie(self):
        """
        Authenticate calls against authentication endpoint
        :return: cookie to pass with each subsequent request
        """
        SMAX_AUTH = '{}/auth/authentication-endpoint/authenticate/login?TENANTID={}'. \
            format(self.base_url, self.tenant_id)
        payload = {'Login': '{}'.format(self.user_name), 'Password': '{}'.format(self.password)}
        payload = json.dumps(payload)
        smax_token = requests.post(SMAX_AUTH, data=payload)
        auth_c = str(smax_token.content.decode("utf-8"))
        cookie_smax = {'LWSSO_COOKIE_KEY': '{0}'.format(auth_c)}
        return cookie_smax

    @staticmethod
    def store_output(function):
        """
        Simple function to store output of a call as a variable, can be used as help for parsing
        or when running jupyter instance or similar
        :param function: function that provides output
        :return: Saved variable of output of a function
        """
        var = dict(function)
        return var

    @staticmethod
    def parse_output(html_data):
        """
        Parse HTML output where entity returns HTML
        can be called for any call, and is called by default on articles API
        :param html_data: HTML data
        :return: Cleaned text
        """
        parse = re.compile(r'<.*?>')
        return parse.sub('', html_data)

    @staticmethod
    def fix_url_encode(url) -> str:
        """
        Change brackets back to normal brackets since SMAX API
        refuses to accept properly URL encoded string
        :param url: Encoded url to fix
        :return: fixed URL
        """
        return str(url).replace('%28', '(').replace('%2C', ',').replace('%29', ')')

    @staticmethod
    def get_help(function):
        """
        Get help with specific function
        :param function: function to display help for
        :return: Help doc for requested function
        """
        try:
            return function.__doc__
        except Exception as error:
            return 'Please input proper function from classes provided'
