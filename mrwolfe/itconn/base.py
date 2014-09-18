class ITConnector(object):

    """ Base class representing a connector to an issue tracking system,
    to be able to forward issues to an issue tracker. """

    def create_issue(self, issue, connector_instance):

        """ Create the issue in the remote system """


class ITCRegistry(object):

    """ Global registry for connectors

    The registry can take any attrivutes per content type, but the following
    attributes have active use so far:

      class            Actual class for connecto
      label            Front end name of connector
    """

    _connectors = {}

    @staticmethod
    def register(name, register_dict):

        ITCRegistry._connectors[name] = register_dict

    @staticmethod
    def get(name):

        """
        Fetch all details for contenttype with name as a dict.
        """

        return ITCRegistry._connectors.get(name, {})

    @staticmethod
    def get_attr(name, attr, default=None):

        """ Fetch given attr. Return default if not set"""

        return ITCRegistry._connectors.get(name, {}).get(attr, default)

    @staticmethod
    def list_types():

        return ITCRegistry._connectors.keys()
