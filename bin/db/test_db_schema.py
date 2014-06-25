#pylint: skip-file

import unittest
import db_schema
from flask import Flask

## This series of tests handles configuring and connecting to the database
class DBSchemaTest(unittest.TestCase):

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
  def test_db_connection(self):
    db = db_schema.GetDatabaseConnection('db02.db')
    #When Run on djmorrsee's mac!!
    self.assertTrue(str(db.engine.url) == 'sqlite://///Users/djmorrsee/Documents/School/Summer_2014/M&T/Project/db/db02.db')



if __name__ == '__main__':
  unittest.main()
