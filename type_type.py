from type_type_dictionary import *
import winsound


class TypeType():
	def __init__(self):
		# do nothing for now
		return
	
	def start(self):
		dict = TypeTypeDictionary( [["Rio", "rio.wav"], ["Flor","flor.wav"], ["Lumi", "lumi.wav"], ["Nilza", "nilza.wav"]] )
		word = dict.next()
		while 1==1:
			print "Palavra: ",  word[dict.WORD_TEXT]
			winsound.PlaySound( "escreve.wav", winsound.SND_FILENAME )
			winsound.PlaySound( word[dict.WORD_SOUND], winsound.SND_FILENAME )
			var = raw_input("\nEscreve a palavra: ")
			print "\ntu escreveste: ", var
			print " eu escrevi: ", word[dict.WORD_TEXT]
			if var == word[dict.WORD_TEXT ]:
				print "\n============="
				print "\n ESTA CERTO"
				print "\n=============\n\n"
				winsound.PlaySound('correct_alert.wav', winsound.SND_FILENAME)
			else:
				print "\n!!!!!!!!!!!!!!!!!!"
				print "\n tenta outra vez!"
				print "\n!!!!!!!!!!!!!!!!!!\n\n"
				winsound.PlaySound('error_alert.wav', winsound.SND_FILENAME)
			word = dict.next()
		print "\n==========================="
		print "\n Boa, chegaste ao fim!!!! "
		print "\n===========================\n\n"
		

def get_going():
	tt = TypeType();
	tt.start();
				
if __name__ == "__main__":
	get_going()
