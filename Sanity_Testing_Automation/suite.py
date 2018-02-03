__author__ = 'Chennareddy'
import unittest
from xmlrunner import xmlrunner

#from user_signup_login import TestAccount

from user_signup_login import TestAccount
from d import BookHandstand

tests1 = unittest.TestLoader().loadTestsFromTestCase(TestAccount)
tests2 = unittest.TestLoader().loadTestsFromTestCase(BookHandstand)

all_tests = unittest.TestSuite([tests1,tests2])

unittest.TextTestRunner(verbosity=2).run(all_tests)