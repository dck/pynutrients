# -*- coding: utf-8 -*-


class Nutrients(object):

    def __init__(self, provider):
        self.provider = provider

    def set_provider(self, provider):
        self.provider = provider

    def request(self, name):
        pass