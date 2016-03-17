import json

class Database():
    """
    Encapsulation class for the database of the application
    """

    def __init__(self):
        self.path = ""

        self.loaded_database = {}

    def set_path(self, path):
        """
        Sets the path to "path"
        """
        self.path = path

        return True

    def get_path(self):
        """
        Returns the path to the current database
        """
        return self.path

    def load_database(self):
        """
        Loads the database from the path self.path
        """
        # @TODO: Load database

        return True

    def load_database(self, path):
        """
        Loads a database from the path "path" & sets self.path to path
        """
        self.path = path

        # Loading database
        return self.load_database()
