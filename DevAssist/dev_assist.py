from DevAssist.speech import Speech, SpeechDriver
from DevAssist.process_input import ProcessInput
from DevAssist.utils.module_loading import import_module


class DevAssist():
    """
    Main DevAssist class which runs all of the subprocesses.
    """

    def __init__(self, **kwargs):
        """
        Set up instance of DevAssist
        """
        # Setting up variables
        self.input_processor = ProcessInput()
        self.conversation = []

        # Parsing options
        if kwargs.get("speech_adapter") is not None:
            self.speech = Speech(**kwargs)
            self.speech_driver = SpeechDriver(self.speech)
            self.speech_driver.start()
        else:
            self.speech_driver = None

        modules = kwargs.get("modules", [
            "DevAssist.modules.file_runner.FileRunner",
            "DevAssist.modules.run_tests.TestRunner"
        ])

        for my_module in modules:
            self.add_adapter(my_module, **kwargs)

    def process(self, user_input):
        """
        Process input & generate a response.
        """
        # Processing input
        processed_input = user_input
        if self.speech_driver is not None:
            processed_input = self.speech_driver.get_queue()

        # Generating a response
        response = self.input_processor.process(processed_input)

        # Adding the processed input and response to the conversation
        self.conversation.append([processed_input, response])

        # Return the generated response
        return response

    def add_adapter(self, my_module, **kwargs):
        """
        Add the specified module into DevAssist.
        """
        NewAdapter = import_module(my_module)
        adapter = NewAdapter(**kwargs)

        self.input_processor.add_module(adapter)
