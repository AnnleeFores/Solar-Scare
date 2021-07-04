import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from time import sleep 
from datetime import *
import subprocess
import os

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

cs = digitalio.DigitalInOut(board.D5)

mcp = MCP.MCP3008(spi, cs)

chan = AnalogIn(mcp, MCP.P0)

pump = digitalio.DigitalInOut(board.D18)
pump.direction = digitalio.Direction.OUTPUT

subprocess.call('alsactl --file ./audio_sensor_scripts/asound.state restore', shell=True)

while True:
    if chan.value < 10000:
        print('Sensor value =',chan.value)
    else: 
        print('Sensor value =',chan.value)
        print('')
        print('Running pump for 3sec')
        pump.value = True
        sleep(5)
        pump.value = False
        print('')
        subprocess.call('arecord --format=S16_LE --rate=16000 --file-type=wav --duration=10 --use-strftime %d-%m-%Y/%H-%M-%v.wav', shell=True)
        print('')
        sleep(2)
    sleep(1.5)
