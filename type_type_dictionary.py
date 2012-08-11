class TypeTypeDictionary():
	dict = [];
		
	def __init__(self, words=[]):
		self.dict = words;
		return
		
	def first (self):
		return self.dict[0];
		
	def size (self):
		return len( self.dict );