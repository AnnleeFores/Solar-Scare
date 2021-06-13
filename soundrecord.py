from time import sleep
from datetime import *
import time
import subprocess
import os

working_file = 'currentlyRecording.wav'


def setup():

    try:
        # Load alsactl file - increased microphone volume level
        subprocess.call('alsactl --file ./audio_sensor_scripts/asound.state restore', shell=True)
        return True
    except:
        raise EnvironmentError
               
  
