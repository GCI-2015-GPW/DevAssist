from DevAssist import DevAssist
from DevAssist.utils.input_normalizer import input_function

my_devassist = DevAssist()

while True:
    user_input = input_function()

    # Leave if the user is done
    if user_input == "quit":
        exit(0)

    # Generate response
    response = my_devassist.process(user_input)

    # Print response
    print(response)
