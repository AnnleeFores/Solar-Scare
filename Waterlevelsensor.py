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

while True:
    sensorvalue = chan.value
    print(sensorvalue)
    print(chan.voltage)
    sleep(1.5)