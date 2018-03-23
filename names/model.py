from models import Component


class Model(object):
    def __init__(self):
        self.pattern = ''

    def set_pattern(self, value):
        self.pattern = value

    def get_pattern(self):
        return self.pattern

    @staticmethod
    def new_component(type_of, prefix, description, pattern, arguments):
        """

        :param type_of: the type of component i.e. 'SMD' or 'PTH'
        :param prefix: the prefix of the pattern i.e. 'SOT'
        :param description: the long description of the component
        :param pattern: the pattern used to create the IPC name
        :param arguments: a string with the argument to fill pattern,
                          separated by comma
        :return:
        """
        component = Component.objects.create(type_of=type_of.upper(),
                                             prefix=prefix.upper(),
                                             description=description,
                                             pattern=pattern,
                                             arguments=arguments)
        return component

    @staticmethod
    def get_component(type_of, prefix, description):
        """
        :param type_of: the type of component i.e. 'SMD' or 'PTH'
        :param prefix: the prefix of the pattern i.e. 'SOT'
        :param description: the long description of the component
        :return: the new Component object created
        """
        return Component.objects.filter(type_of=type_of.upper(),
                                        prefix=prefix.upper(),
                                        description=description).first()

    @staticmethod
    def get_all_components():
        """
        :return: the list of all components
        """
        return Component.objects.order_by('description').all()

    @staticmethod
    def get_components_by_type(type_of):
        """
        :param type_of: the type of component i.e. 'SMD' or 'PTH'
        :return: the list of all components by type
        """
        return Component.objects.filter(
            type_of=type_of).order_by('description').all()
