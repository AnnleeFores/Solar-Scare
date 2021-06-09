import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from time import sleep 

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

cs = digitalio.DigitalInOut(board.D5)

mcp = MCP.MCP3008(spi, cs)

chan = AnalogIn(mcp, MCP.P0)

pump = digitalio.DigitalInOut(board.D18)
pump.direction = digitalio.Direction.OUTPUT


while True:
    if chan.value < 10000:
        pump.value = False
        print(chan.value)
    else: 
        pump.value = True
        print(chan.value)
    sleep(1.5)
