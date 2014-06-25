""" Data Conversions
  This file contains functions for converting module data into meaningful information
"""

VOLTAGE = 3.3

class ConversionError(Exception):
  """ Exception Class for Data Conversion Errors """
  def __init__(self, msg):
    super(ConversionError, self).__init__(msg)

def IntToTemp(reading):
  """ Converts a pcDuino reading into degrees farenheight

  Args:
    reading (int): 12 bit integer value
  Returns:
    float. The temperature value
  """
  CheckReadingType(reading)
  CheckReadingBounds(reading)

  voltage = (reading * VOLTAGE) / 4096.0
  tempC = (voltage - 0.5) * 100.0
  tempF = (tempC * 9.0 / 5.0) + 32.0

  return tempF

def IntToLight(reading):
  """ Converts a pcDuino reading into a percentage

  Args:
    reading (int): 12 bit integer value
  Returns:
    float. The light intensity percentage
  """
  CheckReadingType(reading)
  CheckReadingBounds(reading)

  return (reading / 4096.0) * 100


def CheckReadingType(reading):
  """ Asserts that the reading is of type int

  Args:
    reading (int): 12 bit integer value
  Returns:
    bool. Assertion that reading is an int
  """
  if(type(reading) is not int):
    raise ConversionError("Conversion Must Be On Integers!")

## Asserts That the reading is 12 bits
def CheckReadingBounds(reading):
  """ Asserts That the reading is 12 bits

  Do this after calling CheckReadingType on readings

  Args:
    reading (int): 12 bit integer value
  Returns:
    bool. Assertion that reading is 12 bits
  """
  if(reading < 0 or reading > 4096):
    raise ConversionError("Conversion Works Only On 12 Bit Integers!")
