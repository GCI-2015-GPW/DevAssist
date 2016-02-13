from DevAssist import DevAssist
from DevAssist.utils.input_normalizer import input_function

my_devassist = DevAssist(
    modules=[
        "DevAssist.modules.file_runner.FileRunner",
        "DevAssist.modules.run_tests.TestRunner"
    ]
)

while True:
    user_input = input_function()

    # Leave if the user is done
    if user_input == "quit":
        exit(0)

    # Generate response
    response = my_devassist.process(user_input)

    # Print response
    print(response)
