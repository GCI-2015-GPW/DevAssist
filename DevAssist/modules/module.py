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

    def should_process(self, user_input):
        """
        Returns whether or not the module should. This allows for a number of
        improvements over a system without this, including:
        - Reduction of # of API calls : You might have to call an API when
            running a module, which this prevents by not running the module
        - Less time to process : Some modules might be able to condense
            run time by a lot. Over many modules, this could reduce the total
            time of running the modules by a lot
        """
        raise ModuleNotImplemented()

    def set_context(self, context):
        """
        Set the module's context
        """
        self.context = context
