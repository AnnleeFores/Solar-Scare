import subprocess
from time import sleep


def movefile():
    command = 'mv ~/solar-scare/server/wingbeats_pi/src/*.wav ~/solar-scare/server/wingbeats_pi/test'
    subprocess.call(command, shell=True)


