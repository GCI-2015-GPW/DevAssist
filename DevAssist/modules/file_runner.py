from DevAssist.utils.extractor import ExtractImportantInformation
from DevAssist.modules.module import Module

import subprocess


class FileRunner(Module):
    """
    Runs a program file. Current list of supported languages:
    - python
    """

    def __init__(self, **kwargs):
        self.name = ""
        self.path = ""

        self.extractor = ExtractImportantInformation()

    def process(self, user_input):
        """
        Runs a file with the name 'name' located at 'path'. In addition to
        running the file, the program does automatic language detection to
        determine what language the program is (to figure out how to run
        it).
        """
        # Extract the important information
        self.path, self.name = self.extractor.extract_program_information(user_input)

        # Determine what language the program is
        program_type = self.determine_program_type(self.path, self.name)

        # If the file is python, run it the specific way
        # @TODO: Make it work without shell=True
        if program_type == "python":
            subprocess.Popen("python " + self.path + self.name, shell=True)

        return "GOING THROUGH FILE_RUNNER.py...", 1

    def determine_program_type(self, path, name):
        """
        Determines the type of file that is being asked to run.
        This in turn allows DevAssist to run the file properly.
        """

        return "test"
