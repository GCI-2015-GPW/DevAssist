import platform
import subprocess

"""
This is a standalone script that installs the required dependencies to run. It
*should* be platform independent, and should work regardless of what platform
you are running it on.

To install dependencies, download the DevAssist source and run this script by
running "python install_dependencies.py"
"""

# Identifying host platform
host_platform = platform.system()

def install_dependencies():
    """
    Installs dependencies for DevAssist
    """
    # Darwin = Mac OSX
    if host_platform == "Darwin":
        # Installing portaudio
        # @TODO: Rewrite to not use shell=True
        print("Installing portaudio...\n")
        portaudio = subprocess.Popen(["brew install portaudio"], shell=True)
        portaudio.communicate()
        print("\nportaudio has been installed...")

        # Installing pyaudio
        # @TODO: Rewrite to not use shell=True
        print("Installing pyaudio...\n")
        pyaudio = subprocess.Popen(["pip install pyaudio"], shell=True)
        pyaudio.communicate()
        print("\npyaudio has been installed...")
    elif host_platform == "Linux":
        # Installing dependencies for portaudio
        # @TODO: Rewrite to not use shell=True
        print("Installing portaudio & dependencies...\n")
        portaudio = subprocess.Popen(["apt-get install portaudio19-dev python-all-dev python3-all-dev"], shell=True)
        portaudio.communicate()
        print("\nportaudio & dependencies have been installed...")

        # Installing pyaudio
        # @TODO: Rewrite to not use shell=True
        print("Installing pyaudio...\n")
        pyaudio = subprocess.Popen(["pip install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio"], shell=True)
        pyaudio.communicate()
        print("\npyaudio has been installed...")

if __name__ == "__main__":
    install_dependencies()
