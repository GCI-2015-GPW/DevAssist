from DevAssist.speech import Speech, SpeechDriver
from DevAssist.process_input import ProcessInput


class DevAssist():
    """
    Main DevAssist class which runs all of the subprocesses.
    """

    def __init__(self, **kwargs):
        """
        Set up instance of DevAssist
        """
        # Parsing options
        if kwargs.get("speech_adapter") is not None:
            self.speech = Speech(**kwargs)
            self.speech_driver = SpeechDriver(self.speech)
            self.speech_driver.start()
        else:
            self.speech_driver = None

        self.input_processor = ProcessInput()

        self.conversation = []

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
