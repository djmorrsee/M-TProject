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
    ## Function takes a 12 bit uint (0, 4096)
    def conv(val) :
      return 32 + (((val * 3.3) / 4096.0 - 0.5) * 100.0) * 9.0/5.0

    for i in range(0, 4097) :
      self.assertEqual(conversions.IntToTemp(i), conv(i), "Temp Conversion Not Correct For " + str(i))

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
