## @package graphs
# This file contains functions for converting module data into meaningful information

VOLTAGE = 3.3

## Converts a 12 bit integer into degrees F
def IntToTemp(reading):
  voltage = (reading * VOLTAGE) / 4096.0
  tempC = (voltage - 0.5) * 100.0
  tempF = (tempC * 9.0 / 5.0) + 32.0
  return round(tempF, 2)

## Converts a 12 bit integer into a meaningful light reading
# I did not find a meaningful conversion to a physical property, we might
# just have 'off', 'dim' and 'bright' as our meanings
def IntToLight(reading):
  return reading
