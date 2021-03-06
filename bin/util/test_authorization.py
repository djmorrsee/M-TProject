#pylint: skip-file
#Copyright (C) 2014 Andrey Shprengel <andrey.shprengel@colorado.edu> Daniel Morrissey <daniel.morrissey@colorado.edu>
#This work is free. You can redistribute it and/or modify it under the
#terms of the Do What The Fuck You Want To Public License, Version 2,
#as published by Sam Hocevar. See the COPYING file for more details.
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
