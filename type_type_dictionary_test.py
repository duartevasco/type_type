from type_type_dictionary import *
import unittest
 
class TypeTypeDictionaryTest(unittest.TestCase):

	def setUp(self):
		#do nothing for now
		return
	
	def testICanCreateAnEmptyDictionaryTest(self):
		dict = TypeTypeDictionary();
		self.assertNotEqual(dict, None);
	
	def testICanCreateADictionaryWithOneWord(self):
		dict = TypeTypeDictionary( "one" );
		self.assertNotEqual(dict, None);
	
	def tearDown(self):
		#do nothing for now
		return
		
suite = unittest.TestLoader().loadTestsFromTestCase(TypeTypeDictionaryTest)
unittest.TextTestRunner(verbosity=2).run(suite)