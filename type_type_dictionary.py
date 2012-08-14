class TypeTypeDictionary():
	dict = [];
	next_item = 0;
	WORD_TEXT = 0;
	WORD_SOUND = 1;
		
	def __init__(self, words=[]):
		self.dict = words;
		return
		
	def next (self):
		self.next_item += 1
		return self.dict[self.next_item - 1];
		
	def size (self):
		return len( self.dict );