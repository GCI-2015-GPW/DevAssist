from DevAssist.modules.module import Module


class TestRunner(Module):
    """
    Runs the tests for a project. Currently only supports the following
    testing frameworks:
    - nose
    """

    def __init__(self, **kwargs):
        self.testing_suite = "nose"
        self.test_path = ""

    def process(self, user_input):
        """
        Run the tests for the project located at path 'path' using the
        testing suite 'testing_suite'
        """

        return "GOING THROUGH RUN_TESTS.py...", 1
