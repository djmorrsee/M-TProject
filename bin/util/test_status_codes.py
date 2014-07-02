#pylint: skip-file
#Copyright (C) 2014 Andrey Shprengel <andrey.shprengel@colorado.edu> Daniel Morrissey <daniel.morrissey@colorado.edu>
#This work is free. You can redistribute it and/or modify it under the
#terms of the Do What The Fuck You Want To Public License, Version 2,
#as published by Sam Hocevar. See the COPYING file for more details.
import unittest
import status_codes

## This series of tests handles configuring and connecting to the database
class StatusCodeTest(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		pass

	@classmethod
	def tearDownClass(self):
		pass

	def setUp(self):
		pass

	def tearDown(self):
		pass

	### Authored Tests
	def test_valid_code(self):
		self.assertEqual(status_codes.GetCode(701), 'Operation Successful', 'Valid Code Not Found')

	def test_invalid_code(self):
		self.assertEqual(status_codes.GetCode(999), '**Bad Code**', 'Invalid Code Not Recognized')

	def test_bad_type(self):
		self.assertEqual(status_codes.GetCode('701'), '**Bad Code**', 'Invalid Code Not Recognized')

if __name__ == '__main__':
	unittest.main()
