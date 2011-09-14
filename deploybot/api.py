#!/usr/bin/python2.5

import requests
import sys
import simplejson as json

class BambooApi:
    def __init__(self, config):
        self.config = config

    def get_url(self, resource):
        base_url = self.config.get_bamboo_api_root()
        return "%s%s&os_authType=basic" % (base_url, resource)

    def get_auth(self):
        api_user = self.config.get_bamboo_api_user()
        api_password = self.config.get_bamboo_api_password()

        return api_user, api_password

    def get_headers(self):
        headers = {}
        headers["Content-Type"] = "application/json"
        headers["Accept"] = "application/json"

        return headers

    def get(self, resource):
        return self.request(url=self.get_url(resource), 
                            headers=self.get_headers(), 
                            auth=self.get_auth())

    def request(self, url, auth, headers):
        r = requests.get(url, auth=auth, headers=headers)
        return json.loads(r.content)








