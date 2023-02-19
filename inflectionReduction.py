from util import *
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet')

# Add your import statements here




class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""

		reducedText = []
		lemmatizer = WordNetLemmatizer()
		for token_list in text:
			for i in range(len(token_list)):
				token_list[i] = lemmatizer.lemmatize(token_list[i])
			reducedText.append(token_list)
		#Fill in code here
		
		return reducedText


