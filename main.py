# from my_module import foo, person
import modules.my_module as spam
from color50 import rgb, constants

spam.foo(spam.person)

my_color = rgb(204, 204, 0)

print(constants.BRIGHT_MAGENTA + str(dir(spam)) + constants.RESET)

# To create a vitrual environment (venv) in terminal we type "python3 -m venv .venv" 
# where the last .venv is the hidden folder name

# We can also type "which python3" to confirm that we are using the venv.

# We can type "pip freeze" in terminal to see what packages our program is dependent on
# "pip freeze > requirements.txt" will export the requirements into a file


print(my_color + "Hello, World!" + constants.RESET)
