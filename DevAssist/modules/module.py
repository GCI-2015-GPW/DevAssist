from DevAssist.utils.exceptions import ModuleNotImplemented


class Module():
    """
    The abstract class that all modules must be a subclass of.
    """

    def process(self, user_input):
        """
        Returns the processed output from the input.
        """
        raise ModuleNotImplemented()

    def set_context(self, context):
        """
        Set the module's context
        """
        self.context = context
