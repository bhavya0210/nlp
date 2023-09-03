print("hello")

import os

import pandas as pd
import nltk
from nltk import word_tokenize
from textstat.textstat import textstatistics
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
print("here")
nltk.download('punkt')


"""
f = open('./stopwords/StopWords_Auditor.txt', "r")
data = f.read()
l1 = data.split('\n')
#print(len(l1))
f.close()

f = open('./stopwords/StopWords_Currencies.txt', "r")
data = f.read()
l2 = data.split('\n')
for i in range(0, len(l2)-1, 1):
    l2[i] = l2[i].split()[0]
#print(len(l2))
f.close()

f = open('./stopwords/StopWords_DatesandNumbers.txt', "r")
data = f.read()
l3 = data.split('\n')
#print(len(l3))
f.close()

f = open('./stopwords/StopWords_Generic.txt', "r")
data = f.read()
l4 = data.split('\n')
#print(len(l4))
f.close()

f = open('./stopwords/StopWords_GenericLong.txt', "r")
data = f.read()
l5 = data.split('\n')
#print(len(l5))
f.close()

f = open('./stopwords/StopWords_Geographic.txt', "r")
data = f.read()
l6 = data.split('\n')
#print(len(l6))
f.close()

f = open('./stopwords/StopWords_Names.txt', "r")
data = f.read()
l7 = data.split('\n')
#print(len(l7))
f.close()

l8 = ['.', '/', ',', '?', ':', ';', "'", '"', '(', ')', '%', '^', '&']
l8 += ['[', ']', '{', '}', '|', '-', '_', '!', '@', '#', '$', '*']

stopwords = l1+l2+l3+l4+l5+l6+l7+l8
#print(len(stopwords))

f = open('./dict/negative-words.txt', 'r')
masterneg = f.read()
masterneg = masterneg.split('\n')

f = open('./dict/positive-words.txt', 'r')
masterpos = f.read()
masterpos = masterpos.split('\n')

pronouns = ['I', 'We', 'we', 'my', 'My', 'ours', 'Ours', 'us', 'Us']

directory = './files'

print("here now")

idx = 0

df = pd.read_csv('./output.csv')
for fname in os.listdir(directory):

    f = open(os.path.join(directory, fname), 'r')
    data = f.read()

    tokenzz = word_tokenize(str(data))
    tokenzz = [token for token in tokenzz if not token in stopwords]
    newdata = [token for token in tokenzz if not token in stopwords]

    negativedict = []
    positivedict = []

    complexwords = []

    score_positive = 0
    score_negative = 0
    polarity = 0
    subjectivity = 0

    wc = 0
    syllables = 0

    lemmatizer = WordNetLemmatizer()

    for word in newdata:
        word = lemmatizer.lemmatize(word)
        if word in masterneg:
            negativedict.append(word)
            score_negative += 1
        elif word in masterpos:
            positivedict.append(word)
            score_positive += 1

    for word in tokenzz:
        word = lemmatizer.lemmatize(word)
        syllables += textstatistics().syllable_count(word)
        if textstatistics().syllable_count(word) > 2:
            complexwords.append(word)
        wc += 1
    
    polarity = (score_positive - score_negative)/(score_positive+score_negative+0.000001)
    subjectivity = (score_positive+score_negative)/(len(newdata)+0.000001)

    sentences = data.split('.')
    words = data.split(' ')

    senlen = []
    senlenf = 0
    for sentence in sentences:
        senlen.append(len(sentence.split(' ')))
    
    for i in senlen:
        senlenf += i

    words = [word for word in words if not word in l8]

    avgsenlen = len(words)/len(sentences)

    complexpercent = len(complexwords)/len(newdata)
    fog_index = 0.4*(avgsenlen + complexpercent)

    complex_wc = len(complexwords)

    syllable_count = syllables/len(newdata)

    personal_pronouns = 0
    word_length = 0

    for word in words:
        if word in pronouns:
            personal_pronouns += 1
        
        word_length += len(word)

    avgwordlen = word_length/len(words)

    #print(score_positive, score_negative, polarity, subjectivity, avgsenlen, complexpercent, fog_index, avgsenlen, complex_wc, wc, syllable_count, personal_pronouns, avgwordlen)      
    df.loc[idx, 'POSITIVE SCORE'] = score_positive
    df.loc[idx, 'NEGATIVE SCORE'] = score_negative
    df.loc[idx, 'POLARITY SCORE'] = polarity
    df.loc[idx, 'SUBJECTIVITY SCORE'] = subjectivity
    df.loc[idx, 'AVG SENTENCE LENGTH'] = avgsenlen
    df.loc[idx, 'PERCENTAGE OF COMPLEX WORDS'] = complexpercent
    df.loc[idx, 'FOG INDEX'] = fog_index
    df.loc[idx, 'AVG NUMBER OF WORDS PER SENTENCE'] = avgsenlen
    df.loc[idx, 'COMPLEX WORD COUNT'] = complex_wc
    df.loc[idx, 'WORD COUNT'] = wc
    df.loc[idx, 'SYLLABLE PER WORD'] = syllable_count
    df.loc[idx, 'PERSONAL PRONOUNS'] = personal_pronouns
    df.loc[idx, 'AVG WORD LENGTH'] = avgwordlen
    df.to_csv('./output.csv', index=False)

    idx += 1   
    print (idx)
    """