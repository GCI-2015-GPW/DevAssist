from DevAssist import DevAssist
from DevAssist.utils.input_normalizer import input_function
import time

my_devassist = DevAssist(
    speech_adapter="recognize_sphinx"
)

while True:
    # Get a response
    response = my_devassist.process("")

    if response != "":
        # Print response
        print(response)

    # Waiting a specific amount of time before printing the result again
    time.sleep(0.05)
