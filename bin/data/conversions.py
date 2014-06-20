## @package graphs
# This file contains functions for converting module data into meaningful information

VOLTAGE = 3.3

## Exception Class for Conversion Errors
class ConversionError(Exception):
  def __init__(self, msg):
    super(ConversionError, self).__init__(msg)

## Converts a 12 bit integer into degrees F
def IntToTemp(reading):
  CheckReadingType(reading)
  CheckReadingBounds(reading)

  voltage = (reading * VOLTAGE) / 4096.0
  tempC = (voltage - 0.5) * 100.0
  tempF = (tempC * 9.0 / 5.0) + 32.0

  return tempF

## Converts a 12 bit integer into a percentage
def IntToLight(reading):
  CheckReadingType(reading)
  CheckReadingBounds(reading)

  return (reading / 4096.0) * 100

## Asserts that the reading is of type int
def CheckReadingType(reading):
  if(type(reading) is not int):
    raise ConversionError("Conversion Must Be On Integers!")


def CheckReadingBounds(reading):
  if(reading < 0 or reading > 4096):
    raise ConversionError("Conversion Works Only On 12 Bit Integers!")
