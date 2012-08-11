from type_type_dictionary import *
import unittest
 
class TypeTypeDictionaryTest(unittest.TestCase):
	ONE_WORD = "one"
	dict = None;

	def setUp(self):
		#do nothing for now
		self.dict = TypeTypeDictionary( self.ONE_WORD );
		return
	
	def testICanCreateAnEmptyDictionaryTest(self):
		self.dict = TypeTypeDictionary();
		self.assertNotEqual(self.dict, None);
	
	def testICanCreateADictionaryWithOneWord(self):
		self.assertNotEqual(self.dict, None);
	
	def testICanCreateADictionaryWithOneWordAndWordIsRetrievedCorrectly(self):
		self.assertEqual(self.dict.first(), self.ONE_WORD );
	
	def testCanGetDictionarySizeCorrectlyWhenCreatingDictionaryWithOneWord(self):
		self.assertEqual(self.dict.size(), 1 );
	
	def tearDown(self):
		#do nothing for now
		return
		
suite = unittest.TestLoader().loadTestsFromTestCase(TypeTypeDictionaryTest)
unittest.TextTestRunner(verbosity=2).run(suite)