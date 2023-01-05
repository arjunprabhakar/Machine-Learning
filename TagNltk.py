import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
# nltk.download()

stopwords=set(stopwords.words('english'))
txt="Welcome to amal jyothi college of engineering." \
    "college was established in two thousand." \
    "The college is under ktu." \
    "College was located in kottayam."\
    "Amal jyothi is very good for infrastructure ."\
    "The faculity members of amal jyothi is very good"\
    "The courses offered by amal jyothi college is IntMCA,MCA and various Btech programs"

tokenize=sent_tokenize(txt)
for i in tokenize:
    wordlist=word_tokenize(i)
    wordlist=[w for w in wordlist if not w in stopwords]
    tagged=nltk.pos_tag(wordlist)
    print(tagged)


#Chunking
# from nltk import RegexpParser
#
# grammer="NP:{<DT>?<JJ>*<NN>}"
# tokenise=word_tokenize(txt)
# tagg=nltk.pos_tag(tokenise)
# print(tokenise)
# print(tagg)
# RegexParser=RegexpParser(grammer)
# chunked=RegexParser.parse(tagg)
# print(chunked)
# chunked.draw()