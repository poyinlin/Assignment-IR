from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk import stem

#Read the file named "input" and change the content to lower case.
txt = open('input.txt', 'r')
content = txt.read().lower()
txt.close()

#Tokenize the content, and remove the punctuations
content = RegexpTokenizer('[a-z]\w+').tokenize(content)

#Porter's Algorithm
stemmed = []
stemmer = stem.PorterStemmer()
for tag in content:
	stemmed.append(stemmer.stem(tag))

#Remove Stopwords
filtered = [word for word in stemmed if word not in stopwords.words('english')]

#Turn the tokens to a readable format
results = '\n'.join(filtered)

#Write the result back to a txt file named "output"
output = open('output.txt', 'w')
output.write(results)
output.close()
