from DevAssist.utils.stop_words import StopWordsManager
from DevAssist.utils.pos_tagger import POSTagger

import subprocess
import os
import json


class ExtractImportantInformation():
    """
    Extracts the important information from the incoming request from the
    user. This includes:
    - Name of program to run (or do other stuff for)
    - Path to program
    """

    def __init__(self, **kwargs):
        # Initializing variables
        self.program_data = { "name" : "", "path" : "" }

        self.stopwords = StopWordsManager()
        self.tagger = POSTagger()

    def extract_program_information(self, user_input):
        """
        Assuming the user inputed statement is a request for the
        developer assistant, parse the request and return the
        important information.
        """
        # Resetting program_data
        self.program_data["path"] = ""
        self.program_data["name"] = ""

        # Extracting important information from user_input
        self.program_data["path"] = self.extract_path(user_input)
        self.program_data["name"] = self.extract_name(user_input)

        # Return the important information
        return self.program_data["path"], self.program_data["name"]

    def extract_name(self, user_input):
        """
        Return the program's name if it is included somewhere in the
        conversation.
        """
        name = ""

        # The following assumes that the user_input is simply: "run program_x"
        # @TODO: Change this to a more advanced parsing of the user_input. It
        #   requires additional functions within the chatterbot.utils module
        #   and some more thought on how to implement a better system
        # @TODO: Implement more ways a user can communicate the name for
        #   a program
        has_asked_run = False
        for token in self.tagger.tokenize(user_input):
            if has_asked_run:
                if "/" in token:
                    name = token.split("/")[len(token.split("/")) - 1]
                else:
                    name = token
                break

            if "run" in token:
                has_asked_run = True

        return name

    def extract_path(self, user_input):
        """
        Return the program's path if it is included somewhere in the
        conversation.
        """
        path = ""

        # Identifies the path if one is in user_input
        # @TODO: Rewrite to remove false positives (which can be created
        #   easily with the current implementation)
        # @TODO: Implement more ways a user can communicate the path for
        #   a program
        for word in self.tagger.tokenize(user_input):
            if "/" in word:
                if word.endswith("/"):
                    path = word
                else:
                    split = word.split("/")
                    path = "/".join(split[:len(split) - 1]) + "/"
                break

        return path
