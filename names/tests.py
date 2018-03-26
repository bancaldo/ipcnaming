from django.test import TestCase
from names.models import Component
from names.controller import Controller
from names.model import Model


class ComponentTestCase(TestCase):
    def setUp(self):
        self.type_of = "SMT"
        self.prefix = "RESC"
        self.description = "Resistors, Chip"
        self.length = "75"
        self.width = "25"
        self.height = "15"
        self.model = Model()
        self.controller = Controller(self.model)
        self.component = Component.objects.create(type_of='SMT', prefix='RESC',
                                                 description = "Resistors, Chip",
                                                 pattern='RESC{}{}X{}',
                                                 arguments="Body Length, Body Width, Height")

    def test_create_component(self):
        component = Component.objects.create(type_of='SMT', prefix='RESC1',
                                             description = "Resistors, Chip",
                                             pattern='RESC1{}{}X{}',
                                             arguments="Body Length, Body Width, Height")
        self.assertTrue(len(self.controller.get_components_by_type('SMT')) == 2)

    def test_get_component(self):
        component = self.controller.get_component(type_of='SMT', prefix='RESC',
                                                  description = "Resistors, Chip")
        self.assertEqual(self.component, component)

    def test_pattern_correctly_generated(self):
        component = self.controller.get_component(self.type_of,
                                                  self.prefix, self.description)
        self.controller.set_pattern(component.pattern)
        data = (self.length, self.width, self.height)
        self.assertEqual(self.controller.create_name(data), "RESC7525X15")
