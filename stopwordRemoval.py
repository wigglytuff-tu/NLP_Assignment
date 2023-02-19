from util import *
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

# Add your import statements here




class StopwordRemoval():

	def fromList(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""
		stop_words = set(stopwords.words('english'))
		stopwordRemovedText = []
		for i in range(len(text)):
			stopwordRemovedText.append([word for word in text[i] if word.lower() not in stop_words])

		#Fill in code here

		return stopwordRemovedText




	