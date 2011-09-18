#!/usr/bin/python2.5

class Environments:
    
    def __init__(self, config):
        self.config = config

    def list(self):
        return self.config.get_environments()
