from type_type import *
import unittest
 
class TypeTypeTest(unittest.TestCase):

	def setUp(self):
		#do nothing for now
		return
	
	
	def tearDown(self):
		#do nothing for now
		return
		
suite = unittest.TestLoader().loadTestsFromTestCase(TypeTypeTest)
unittest.TextTestRunner(verbosity=2).run(suite)