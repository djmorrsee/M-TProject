import time
from adc import analog_read

VOLT = 3.0

TEMP_PIN = 3
LIGHT_PIN = 2

def delay(ms):
	time.sleep(ms / 1000.0)

def readTemp():
	value = analog_read(TEMP_PIN)
	voltage = (value * VOLT) / 4096.0	
	tempC = (voltage - 0.5) * 100.0
	tempF = (tempC * 9.0 / 5.0) + 32.0

	print('Voltage: ' + str(voltage) + ' TempC: ' + str(tempC) + ' TempF ' + str(tempF))

def readLight():
	value = analog_read(LIGHT_PIN)
	print('Intensity: ' + str(value))


while (1):
	readTemp()
	readLight()
	delay(1000)
