from DevAssist.speech import Speech, SpeechDriver


class DevAssist():

    def __init__(self, **kwargs):
        self.speech = Speech(**kwargs)
        self.speech_driver = SpeechDriver(self.speech)

        self.speech_driver.start()

    def process(self, user_input):
        """
        Process input & generate a response.
        """

        self.speech_driver.get_queue()
