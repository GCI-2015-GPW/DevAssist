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

    def should_process(self, user_input):
        """
        Determine whether or not the test runner should be run.
        """
        # @TODO: Implement a proper should_process method

        return 1

    def process(self, user_input):
        """
        Run the tests for the project located at path 'path' using the
        testing suite 'testing_suite'
        """
        # @TODO: Implement a proper process method

        return "GOING THROUGH RUN_TESTS.py...", 0
