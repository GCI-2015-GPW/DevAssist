import speech_recognition
from multiprocessing import Queue


class Speech():

    def __init__(self, **options):
        self.recognizer = speech_recognition.Recognizer()
        self.microphone = speech_recognition.Microphone()

        self.recognizer_function = options.get(
            "speech_adapter", "recognize_sphinx"
        )

        self.queue = Queue(maxsize=7)
        self.stop_listening = None

    def connect(self):
        """
        Prepare the system to begin listening.
        """
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)

        stop_listening = self.recognizer.listen_in_background(
            self.microphone,
            self.callback
        )

    def disconnect(self):
        if stop_listening:
            self.stop_listening()

    def callback(self, recognizer, audio):
        """
        Process mic input.
        """
        recognizer_function = getattr(recognizer, self.recognizer_function)

        print("IN CALLBACK")

        try:
            result = recognizer_function(audio)
            self.queue.put(result)
        except speech_recognition.UnknownValueError:
            self.queue.put("I was not able to hear what you said")


class SpeechDriver():

    def __init__(self, connection):
        self.connection = connection

    def start(self):
        """
        Start listening in the microphone
        """
        self.connection.connect()

    def stop(self):
        """
        Disconnect the microphone and stop listening
        """
        self.connection.disconnect()

    def get_queue(self):
        """
        Return the queue (which is the generated audio)
        """
        print("PRINTING QUEUE")
        print( str(self.connection.queue.get()) )
        print("PRINTED QUEUE")
        return self.connection.queue.get()
