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

  :param reading: pcDuino Temperature Sensor Reading
  :type reading: 12 bit int

  **reading** type and resolution are checked in function

  :returns: float -- The temperature value
  """
  CheckReadingType(reading)
  CheckReadingBounds(reading)

  voltage = (reading * VOLTAGE) / 4096.0
  tempC = (voltage - 0.5) * 100.0
  tempF = (tempC * 9.0 / 5.0) + 32.0

  return tempF

def IntToLight(reading):
  """ Converts a pcDuino reading into a percentage

  :param reading: pcDuino Light Sensor Reading
  :type reading: 12 bit int

  **reading** type and resolution are checked in function

  :returns: float -- The light intensity percentage
  """
  CheckReadingType(reading)
  CheckReadingBounds(reading)

  return (reading / 4096.0) * 100


def CheckReadingType(reading):
  """ Asserts that the reading is of type int

  :param reading: pcDuino Sensor Reading
  :type reading: 12 bit int

  :returns: bool -- Assertion of int type
  """
  if(type(reading) is not int):
    raise ConversionError("Conversion Must Be On Integers!")

def CheckReadingBounds(reading):
  """ Asserts That the reading is 12 bits

  Do this after calling CheckReadingType on readings

  :param reading: pcDuino Sensor Reading
  :type reading: 12 bit int

  :returns: bool -- Assertion of 12 bit resolution
  """
  if(reading < 0 or reading > 4096):
    raise ConversionError("Conversion Works Only On 12 Bit Integer Values!")

def MakeTimeStamp():
  """ Helper Method to Create a UTC Timestamp

  :returns: UTC/POSIX Time Stamp -- Assumes time zones don't change.
  """
  return time.mktime(datetime.now().timetuple())

def GetLocalTimeString(utc_stamp):
  """ Helper Method To Get a datetime object from utc stamp

  :param utc_stamp: UTC/POSIX Time Stamp
  :type utc_stamp: float
  """
  return datetime.fromtimestamp(utc_stamp)
