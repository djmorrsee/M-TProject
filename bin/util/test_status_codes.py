#pylint: skip-file

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
