from util import *
from nltk.tokenize import TreebankWordTokenizer
import re


# Add your import statements here




class Tokenization():

	def naive(self, text):
		"""
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = []
		exp = r"\s+"
		for sentence in text:
			sentence = re.sub(r'[^\w\s]', ' ', sentence) # remove punctuations
			sentence = sentence.strip() # Remove trailing whitespaces
			sentence = " ".join(sentence.split()) # Remove extra whitespaces within sentence
			tokenizedText.append(re.split(exp,sentence))



		#Fill in code here

		return tokenizedText



	def pennTreeBank(self, text):
		"""
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = []
		for sentence in text:
			tokenizedText.append(TreebankWordTokenizer().tokenize(sentence))


		#Fill in code here

		return tokenizedText