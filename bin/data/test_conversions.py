#pylint: skip-file
#Copyright (C) 2014 Andrey Shprengel <andrey.shprengel@colorado.edu> Daniel Morrissey <daniel.morrissey@colorado.edu>
#This work is free. You can redistribute it and/or modify it under the
#terms of the Do What The Fuck You Want To Public License, Version 2,
#as published by Sam Hocevar. See the COPYING file for more details.
import unittest
import conversions

class ConversionsTest(unittest.TestCase):

  def setUp(self):
    pass
  def tearDown(self):
    pass

  ## Authored Tests
  ## IntToTemp
  def test_int_to_temp(self):
    def close_conv(val) :
      return 32 + (((val * 3.3) / 4096 - 0.5) * 100) * 9/5

    val = close_conv(2048)
    conv_val = conversions.IntToTemp(2048)
    self.assertEqual(val, conv_val)

  def test_negative_int_to_temp(self):
    self.assertRaises(conversions.ConversionError, conversions.IntToTemp, -1)

  def test_large_int_to_temp(self):
    self.assertRaises(conversions.ConversionError, conversions.IntToTemp, 4097)

  def test_type_err_int_to_temp(self):
    self.assertRaises(conversions.ConversionError, conversions.IntToTemp, 'Hello')

  ## IntToLight
  def test_int_to_light(self):
    for i in range(0, 4097):
      self.assertEqual(conversions.IntToLight(i), 100 * i / 4096.0, "Light Conversion Not Correct For " + str(i))

  def test_negative_int_to_light(self):
    self.assertRaises(conversions.ConversionError, conversions.IntToLight, -1)

  def test_large_int_to_light(self):
    self.assertRaises(conversions.ConversionError, conversions.IntToLight, 4097)

  def test_type_err_int_to_light(self):
    self.assertRaises(conversions.ConversionError, conversions.IntToLight, 'Hello')


if __name__ == '__main__':
  unittest.main()
