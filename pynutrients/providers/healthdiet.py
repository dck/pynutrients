# -*- coding: utf-8 -*-

from pynutrients.providers.provider import Provider
from pynutrients import Product

class HealthDiet(Provider):

    def __init__(self):
        Provider.__init__(self)
        pass

    def request_product(self, name):
        pass