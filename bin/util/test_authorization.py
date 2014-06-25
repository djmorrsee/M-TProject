#pylint: skip-file

import unittest
import authorization

## This series of tests handles configuring and connecting to the database
class AuthorizationTest(unittest.TestCase):

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
	def test_build_auth_ids(self):
		return self.assertEqual(authorization.auth_ids, [123, 321], 'Error Loading Auth IDs')

	def test_valid_auth_data(self):
		data = { "auth_id":None }
		return self.assertTrue(authorization.VerifyAuthData(data))

	def test_invalid_auth_data(self):
		data = { "gauth_id":None }
		return self.assertTrue(not authorization.VerifyAuthData(data))

	def test_valid_auth_id(self):
		data = { "auth_id":123 }
		return self.assertTrue(authorization.AuthorizeAuthData(data))

	def test_invalid_auth_id(self):
		data = { "auth_id":1234 }
		return self.assertTrue(authorization.AuthorizeAuthData(data))


if __name__ == '__main__':
	unittest.main()
