from type_type_dictionary import *
import unittest
 
class TypeTypeDictionaryTest(unittest.TestCase):
	ONE_WORD = ['one', "one.wav"]
	TWO_WORD = ['two', "two.wav"]
	ONE_WORD_TEXT = 'one'
	ONE_WORD_WAVFILE = "one.wav"
	NUMBER_ONE = 1
	dict = None;

	def setUp(self):
		#do nothing for now
		self.dict = TypeTypeDictionary( [self.ONE_WORD] );
		return
	
	def testICanCreateAnEmptyDictionaryTest(self):
		self.dict = TypeTypeDictionary();
		self.assertNotEqual(self.dict, None);
	
	def testICanCreateADictionaryWithOneWord(self):
		self.assertNotEqual(self.dict, None);
	
	def testICanCreateADictionaryWithOneWordAndWordIsRetrievedCorrectly(self):
		self.assertEqual(self.dict.next(), self.ONE_WORD );
	
	def testCanGetDictionarySizeCorrectlyWhenCreatingDictionaryWithOneWord(self):
		self.assertEqual(self.dict.size(), self.NUMBER_ONE );
		
	def testCanGetDictionarySizeCorrectlyWhenCreatingDictionaryWithTwoWords(self):
		self.dict = TypeTypeDictionary( [self.ONE_WORD, self.TWO_WORD] );
		self.assertEqual(self.dict.size(), 2);

	def testCanBothWordsInDictionaryByCallingFirstAndNext(self):
		self.dict = TypeTypeDictionary( [self.ONE_WORD, self.TWO_WORD] );
		self.assertEqual(self.dict.next(), self.ONE_WORD);
		self.assertEqual(self.dict.next(), self.TWO_WORD);
	
	def testCanGetBothWordTextAndWAVFileWhenReceivingNextObject(self):
		next_item = self.dict.next();
		self.assertEqual(next_item[0], self.ONE_WORD_TEXT);
		self.assertEqual(next_item[1], self.ONE_WORD_WAVFILE);
		
	def tearDown(self):
		#do nothing for now
		return
		
suite = unittest.TestLoader().loadTestsFromTestCase(TypeTypeDictionaryTest)
unittest.TextTestRunner(verbosity=2).run(suite)