import sys
import re
import functools, math
import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import wordnet

sid = SentimentIntensityAnalyzer()

def get_trends(tag):
	print(tag)
	tkns_CE=''
	with open('tweets.txt','r', encoding='UTF8') as file:
		for line in file:
			pat = re.compile(tag)
			if pat.search(line.lower()) != None:
				#print(line)
				seg = re.sub(r'[^\x00-\x7f]+',r' ',line)
				seg = re.sub(r'[^a-zA-Z0-9_\s]+', '', seg)
				#print(seg)
				#tokens = word_tokenize(seg)
				#stopw = [i for i in tokens if not i in stop_words]
				result = TextBlob(seg.lower())
				#print(result.tags)
				for word, pos in result.tags:
					if pos == 'JJ':
						if (sid.polarity_scores(word)['compound']) >= 0.5:
						#print(word)
							tkns_CE += ' ' + word

	tkns_CE = tkns_CE.split()
	#print(tkns)
	for i in range(len(tkns_CE)):						
		for syns in wordnet.synsets(tkns_CE[i], pos = 'a'):
			if syns:
				lemmas = syns.lemmas()
				#print(lemmas)
				for l in lemmas:
					for j in range(i,len(tkns_CE)):
						if l.name().lower() == tkns_CE[j]:
							#print(tkns_CE[j],tkns_CE[i])
							tkns_CE[j] = tkns_CE[i]
	fdist = FreqDist(tkns_CE)
	#print(fdist)
	print(fdist.most_common(10))
	
get_trends('clinteastwood')
get_trends('bradleycooper')
get_trends('chriskyle')

	
				
				

			
			
			
			
