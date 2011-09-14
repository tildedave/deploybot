#!/usr/bin/python2.5

class Config:
    
    def __init__(self, parser):
        self.parser = parser
        self.build = None
        self.plan = None

    ## Basic Options

    def get_deploy_command(self):
        return self.parser.get("DEFAULT", "deploy_command")

    def get_deploy_log(self):
        return self.parser.get("DEFAULT", "deploy_log")

    ## Current Build

    def get_build(self):
        return self.build

    def set_build(self, build):
        self.build = build

    def get_plan(self):
        return self.plan

    def set_plan(self, plan):
        self.plan = plan

    ## Bamboo Config Options

    def __get_bamboo_config(self, option):
        return self.parser.get("Bamboo", option)

    def get_bamboo_project(self):
        """Returns the Current Bamboo Project"""
        return self.__get_bamboo_config("project")

    def get_bamboo_api_root(self):
        """Returns the API Root, i.e. http://bamboo.mosso.com/rest/api/latest"""
        return self.__get_bamboo_config("api_root")

    def get_bamboo_api_user(self):
        """Returns the user credential used for BasicAuth on the Bamboo API"""
        return self.__get_bamboo_config("user")

    def get_bamboo_api_password(self):
        """Returns the password credential used for BasicAuth 
           on the Bamboo API"""
        return self.__get_bamboo_config("password")
