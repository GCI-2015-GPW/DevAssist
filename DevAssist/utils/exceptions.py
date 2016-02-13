class ModuleNotImplemented(NotImplementedError):
    """
    This class is the exception thrown when a module is not properly
    created.
    """

    def __init__(self, message="This method must be overridden in a subclass"):
        self.message = message

    def __str__(self):
        return self.message
