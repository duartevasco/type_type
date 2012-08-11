class TypeTypeDictionary():
	dict = [];
		
	def __init__(self, word=[]):
		global dict;
		dict = [];
		dict.append(word);
		return
		
	def first (self):
		return dict[0];
		
	def size (self):
		return 1;