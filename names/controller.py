class Controller(object):
    def __init__(self, model):
        self.model = model

    def set_pattern(self, value):
        self.model.set_pattern(value)

    def get_pattern(self):
        return self.model.get_pattern()

    def create_name(self, data):
        pattern = self.get_pattern()
        return pattern.format(*data)

    def get_component(self, type_of, prefix, description):
        return self.model.get_component(type_of, prefix, description)

    def get_components_by_type(self, type_of):
        components = self.model.get_components_by_type(type_of)
        return ["%s_%s" % (c.prefix, c.description) for c in components]
