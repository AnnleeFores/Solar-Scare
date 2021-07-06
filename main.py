import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from time import sleep 
from datetime import *
import subprocess
import os
import schedule
import sys

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

cs = digitalio.DigitalInOut(board.D5)

mcp = MCP.MCP3008(spi, cs)

chan = AnalogIn(mcp, MCP.P0)

pump = digitalio.DigitalInOut(board.D18)
pump.direction = digitalio.Direction.OUTPUT

subprocess.call('alsactl --file ./audio_sensor_scripts/asound.state restore', shell=True)



def printchan():
    print('Sensor value =',chan.value)


def micpi():
    if chan.value > 10000:
        print('')
        print('Recording audio')
        subprocess.call('arecord --format=S16_LE --rate=16000 --file-type=wav --duration=10 --use-strftime %d-%m-%Y/%H-%M-%v.wav', shell=True)
        print('')

def pumppi():
    if chan.value > 10000:
        print('')
        print('Running pump')
        pump.value = True
        sleep(5)
        pump.value = False
        print('')

schedule.every(5).seconds.do(printchan)
schedule.every(60).seconds.do(micpi)
schedule.every().minute.at(":35").do(pumppi)

while True:
        schedule.run_pending()
        sleep(1)
