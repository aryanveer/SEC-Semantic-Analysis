import nltk
import string
from string import punctuation
from urllib.request import urlretrieve
import urllib.request

punc_list = list(punctuation)
punc_list.append("''")
punc_list.append("'S")
punc_list.append("--")
punc_list.append("..")
punc_list.append("...")
punc_list.append("/PAGE")
punc_list.append("``")
punc_list.append("=======")
punc_list.append("========")
punc_list.append("'/S")
punc_list.append("'/C")
punc_list.append("/CAPTION")
punc_list.append("/TABLE")
punc_list.append('')
punc_list.append("A.")
punc_list.append("ON")

pk=1+2

stop_list = nltk.corpus.stopwords.words('english')
stop_list = stop_list + punc_list

generic_words_list = urllib.request.urlopen("https://www3.nd.edu/~mcdonald/Data/ND_Stop_Words_Generic.txt").read()
generic_words_list = generic_words_list.decode("ASCII")
generic_words_list=generic_words_list.split('\r\n')

names_words_list = urllib.request.urlopen("https://www3.nd.edu/~mcdonald/Data/ND_Stop_Words_Names.txt").read()
names_words_list = names_words_list.decode("ASCII")
names_words_list=names_words_list.split('\r\n')

datesnumbers_words_list = urllib.request.urlopen("https://www3.nd.edu/~mcdonald/Data/ND_Stop_Words_DatesandNumbers.txt").read()
datesnumbers_words_list = datesnumbers_words_list.decode("ASCII")
datesnumbers_words_list=datesnumbers_words_list.split('\r\n')

geography_words_list = urllib.request.urlopen("https://www3.nd.edu/~mcdonald/Data/ND_Stop_Words_Geographic.txt").read()
geography_words_list = geography_words_list.decode("ASCII")
geography_words_list=geography_words_list.split('\r\n')

combined_stopwords_list = generic_words_list + names_words_list + datesnumbers_words_list + geography_words_list + stop_list + list(string.ascii_uppercase)
