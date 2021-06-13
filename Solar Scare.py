from time import sleep
from datetime import *
import subprocess
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

cs = digitalio.DigitalInOut(board.D5)

mcp = MCP.MCP3008(spi, cs)

chan = AnalogIn(mcp, MCP.P0)

pump = digitalio.DigitalInOut(board.D18)
pump.direction = digitalio.Direction.OUTPUT

subprocess.call('alsactl --file ./audio_sensor_scripts/asound.state restore', shell=True)

if chan > 15000:
    while True:
        subprocess.call('arecord --format=S16_LE --rate=16000 --file-type=wav --duration=10 --use-strftime %d-%m-%Y/%H-%M-%v.wav', shell=True)
        sleep(590)

if chan > 15000:
    while True:
        pump.value = True
        print(chan.value)
        sleep(1800)  
