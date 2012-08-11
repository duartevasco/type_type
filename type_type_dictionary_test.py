from type_type_dictionary import *
import unittest
 
class TypeTypeDictionaryTest(unittest.TestCase):
	ONE_WORD = "one"

	def setUp(self):
		#do nothing for now
		return
	
	def testICanCreateAnEmptyDictionaryTest(self):
		dict = TypeTypeDictionary();
		self.assertNotEqual(dict, None);
	
	def testICanCreateADictionaryWithOneWord(self):
		dict = TypeTypeDictionary( self.ONE_WORD );
		self.assertNotEqual(dict, None);
	
	def testICanCreateADictionaryWithOneWordAndWordIsRetrievedCorrectly(self):
		dict = TypeTypeDictionary( self.ONE_WORD );
		self.assertEqual(dict.first(), self.ONE_WORD );
	
	def tearDown(self):
		#do nothing for now
		return
		
suite = unittest.TestLoader().loadTestsFromTestCase(TypeTypeDictionaryTest)
unittest.TextTestRunner(verbosity=2).run(suite)