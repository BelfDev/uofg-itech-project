import os
import sys
from shutil import which
from subprocess import call

necessary_tools = ["python", "poetry", "pip", "yarn", "npm", "conda"]
uninstalled_tools = []
original_dir = os.getcwd()


def is_installed(name):
    """Check whether `name` is on PATH and marked as executable."""
    return which(name) is not None


def confirm(message):
    """
    Ask user to enter Y or N (case-insensitive).
    :return: True if the answer is Y.
    :rtype: bool
    """
    answer = ""
    while answer not in ["y", "n"]:
        answer = input(message).lower()
    return answer == "y"


print("""
 ____  __  ___  __ _  ____  ____ 
(  _ \(  )/ __)(  / )(  __)(  __)
 ) __/ )(( (__  )  (  ) _)  ) _) 
(__)  (__)\___)(__\_)(____)(____)
""")
print("\nWe'll set up the entire project for you!\n")

print("======================================================")
print("Verifying if you have the necessary tools installed...")
print("======================================================")
# Prints the installation verification result
for tool in necessary_tools:
    print('\t\t{:<10s} {:<10s}'.format(tool, str(is_installed(tool))))
    if not (is_installed(tool)):
        # Stores tools which could not be detected
        uninstalled_tools.append(tool)

if uninstalled_tools:
    if "python" in uninstalled_tools:
        print("\nWe really need python!")
        print("https://www.python.org/downloads/release/python-373/")
        sys.exit()
    # Checks for frontend tools
    if "yarn" in uninstalled_tools and "npm" in uninstalled_tools:
        print("\nWe need at least one node package management tool to install frontend packages.")
        print("We recommend installing Yarn")
        print("https://classic.yarnpkg.com/en/docs/install")
        sys.exit()
    # Checks for backend tools
    if "poetry" in uninstalled_tools and "pip" in uninstalled_tools:
        print("\nWe need at least one python package management tool to install backend packages")
        print("We recommend installing Poetry")
        print("https://github.com/python-poetry/poetry")
        sys.exit()

print("\nAll good!")
# Checks and activates the python virtual environment
if "poetry" in uninstalled_tools:
    print("We see you are not using poetry.")
    answer = confirm("\nDo you have your virtual environment activated? [Y/N]\n")
    if answer:
        print("Ok, good. Let's go!\n")
    else:
        print("It will be better if we don't activate it for you.")
        print("Please activate your virtual environment and come back later, ok?")
        sys.exit()
else:
    print("================================================")
    print("Activating the virtual environment via Poetry...")
    print("================================================")
    call('poetry shell', shell=True)

print("\n==================================")
print("Installing backend dependencies...")
print("==================================")
# Delegates the installation of backend packages to Poetry or Pip
if "poetry" in uninstalled_tools:
    call('pip install -r requirements.txt', shell=True)
else:
    call('poetry install', shell=True)

print("\n===================================")
print("Installing frontend dependencies...")
print("===================================")
# Installs frontend dependencies and frontend  files
os.chdir("pickee_frontend")
if "yarn" in uninstalled_tools:
    call('npm install', shell=True)
    print("\n=============================")
    print("     Building frontend...")
    print("=============================")
    call('npm build', shell=True)
else:
    call('yarn install', shell=True)
    print("\n=============================")
    print("     Building frontend...")
    print("=============================")
    call('yarn build', shell=True)

os.chdir(original_dir)
print("\n=============================")
print("    Generating migrations...")
print("=============================")
call('python manage.py makemigrations', shell=True)

print("\n========================")
print("      Migrating...")
print("========================")
call('python manage.py migrate', shell=True)

print("\n=============================")
print("    Populating database...")
print("=============================")
call('python population_script.py', shell=True)

print("\n=============================")
print("And finally: running the app!")
print("=============================")
call('python manage.py runserver', shell=True)

print("\nEnjoy Pickee!")
