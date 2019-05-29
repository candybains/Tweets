import sys
import re
import functools, math
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()
tags = []
tkns_CE=''
tkns_BC=''
tkns_CK=''
stop_words = set(stopwords.words('english'))
#with open('d:/Prabhkirat/Python/ClintEastwoodTokens.txt', "w", encoding='UTF8') as outfile:
with open('d:/Prabhkirat/Python/tweets.txt','r', encoding='UTF8') as file:
	for line in file:
		pat = re.compile('clinteastwood')
		if pat.search(line.lower()) != None:
			#print(line)
			seg = re.sub(r'[^\x00-\x7f]+',r' ',line)
			seg = re.sub(r'[^a-zA-Z0-9_\s]+', '', seg)
			#print(seg)
			#tokens = word_tokenize(seg)
			#stopw = [i for i in tokens if not i in stop_words]
			result = TextBlob(seg)
			#print(result.tags)
			for word, pos in result.tags:
				if pos == 'JJ':
					if (sid.polarity_scores(word)['compound']) >= 0.5:
					#print(word)
						tkns_CE += ' ' + word
					
		pat2 = re.compile('bradleycooper')
		if pat2.search(line.lower()) != None:
			seg2 = re.sub(r'[^\x00-\x7f]+',r' ',line)
			seg2 = re.sub(r'[^a-zA-Z0-9_\s]+', '', seg2)
			result2 = TextBlob(seg2)
			for word, pos in result2.tags:
				if pos == 'JJ':
					if (sid.polarity_scores(word)['compound']) >= 0.5:
						tkns_BC += ' ' + word
					
		pat3 = re.compile('chriskyle')
		if pat3.search(line.lower()) != None:
			seg3 = re.sub(r'[^\x00-\x7f]+',r' ',line)
			seg3 = re.sub(r'[^a-zA-Z0-9_\s]+', '', seg3)
			result3 = TextBlob(seg3)
			for word, pos in result3.tags:
				if pos == 'JJ':
					if (sid.polarity_scores(word)['compound']) >= 0.5:
						tkns_CK += ' ' + word
				
				
tkns_CE = tkns_CE.split()
#print(tkns)
fdist = FreqDist(tkns_CE)
#print(fdist)
print('Clint Eastwood')
print(fdist.most_common(10))

tkns_BC = tkns_BC.split()
#print(tkns)
fdist2 = FreqDist(tkns_BC)
#print(fdist)
print('Bradley Cooper')
print(fdist2.most_common(10))

tkns_CK = tkns_CK.split()
#print(tkns)
fdist4 = FreqDist(tkns_CK)
#print(fdist)
print('Chris Kyle ')
print(fdist4.most_common(10))
				
				

			
			
			
			
