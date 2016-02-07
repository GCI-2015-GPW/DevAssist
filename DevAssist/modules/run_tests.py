from DevAssist.utils.extractor import ExtractImportantInformation


class RunTests():
    """
    Runs the tests for a project. Currently only supports the following
    testing frameworks:
    - nose
    """

    def __init__(self):
        self.testing_suite = "nose"
        self.test_path = ""

        self.extractor = ExtractImportantInformation()

    def run_tests(self, path, testing_suite):
        """
        Run the tests for the project located at path 'path' using the
        testing suite 'testing_suite'
        """
        pass
