from DevAssist import DevAssist

my_jarvis = JARVIS()

while True:
    # @TODO: Normalize input from different versions of python
    user_input = raw_input("Human: ")

    # Leave if the user is done
    if user_input == "quit":
        exit(0)

    # Generate response
    response = my_jarvis.process(user_input)

    # Print response
    print response
