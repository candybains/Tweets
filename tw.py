import re
import functools, math
import nltk
#nltk.download('words')
#from nltk.corpus import words, brown, wordnet, stopwords, names
tags = []
with open('tweets.txt','r', encoding='UTF8') as file:
	for line in file:
		tags += re.findall(r'[#][^\s#]+', line)

tags = set(tags)
print('Hashtags')
with open('hasgtags#.txt', "w", encoding='UTF8') as outfile:
	for entries in tags:
		#seg = re.sub('\W+','', entries )
		outfile.write(str(entries))
		outfile.write("\n")
print('Output File')		
class OneGramDist(dict):
	def __init__(self, filename):
		self.gramCount = 0

		for line in open(filename):
			(word, count) = line[:-1].split('\t')
			self[word] = int(count)
			self.gramCount += self[word]

	def __call__(self, key):
		if key in self:
			return float(self[key]) / self.gramCount
		else:
			return 1.0 / (self.gramCount * 10**(len(key)-2))

singleWordProb = OneGramDist('d:/Prabhkirat/Python/one_grams.txt')

def wordSeqFitness(words):
   return functools.reduce(lambda x,y: x+y,(math.log10(singleWordProb(w)) for w in words))
	
def memoize(f):
   cache = {}

   def memoizedFunction(*args):
      if args not in cache:
         cache[args] = f(*args)
      return cache[args]

   memoizedFunction.cache = cache
   return memoizedFunction

@memoize
def segment(word):
   if not word: return []
   word = word.lower() # change to lower case
   allSegmentations = [[first] + segment(rest) for (first,rest) in splitPairs(word)]
   return max(allSegmentations, key = wordSeqFitness)
	
def splitPairs(word):
   return [(word[:i+1], word[i+1:]) for i in range(len(word))]
@memoize
	 
def segmentWithProb(word):
   segmented = segment(word)
   return (wordSeqFitness(segmented), segmented)
	
#print(split_hashtag_to_words_all_possibilities('goldenglobes'))

with open('hasgtagsSeg.txt', "w", encoding='UTF8') as outfile:
	for entries in tags:
		seg = re.sub('\W+','', entries )
		print(seg)
		segmented = segment(seg)
		print(segmented)
		outfile.write(str(entries) + '  -> ' + str(segmented))
		outfile.write("\n")
		print('Done')
		

		
		




	
