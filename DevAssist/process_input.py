

class ProcessInput():
    """
    Processes the input and picks an appropriate response, executes the
    appropriate action.
    """

    def __init__(self):
        self.modules = []

    def add_module(self, adapter):
        """
        Add a module to DevAssist
        """
        self.modules.append(adapter)

    def process(self, user_input):
        """
        Process the incoming statement and decide which modules to use.
        """
        response = "I apologize, but I did not understand the request."
        confidence = -1

        for my_module in self.modules:
            if my_module.should_process(user_input):
                test_response, test_confidence = my_module.process(user_input)

                if test_confidence > confidence and test_confidence != 0:
                    response = test_response
                    confidence = test_confidence

        # Return the generated response
        return response

    def set_context(self, context):
        """
        Set the context for each of the contained modules.
        """

        for my_module in self.modules:
            my_module.set_context(context)
