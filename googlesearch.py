import urllib
from bs4 import BeautifulSoup
import requests
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import operator
import re


def search(text):
    stopwordlist=set(stopwords.words('english'))
    keywords=list(set([w for w in word_tokenize(text) if w not in stopwordlist]))
    #print("keywords")
    #print(keywords)
    text = urllib.parse.quote_plus(text)
    url = 'https://google.com/search?q=' + text
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    result=""
    data=[]
    dicti={}
    i=0

    for g in soup.find_all(class_='st'):
        print(g.text)
        #data.append(g.text)
        #print("length = "+ str(len(g.text)))
        print('-----')
        count=0
        for word in keywords:
            if word.lower() in str(g.text).lower():
                  count+=1
        data.append(re.sub('\((.*?)\)', '', g.text))
        #stopwordsremoved=[w for w in word_tokenize(data[i]) if w not in stopwordlist]
        #dicti[i]=len(set(stopwordsremoved))
        dicti[i]=count
        i+=1
        if len(result) < len(g.text):
           result=g.text
    i=len(keywords)
    print("dict values")
    print(dicti)
    while i> 0:
       best=[k for k,v in dicti.items() if v == i]
       if len(best) >0:
          break
       i-=1
    result=""
    #print("the best values are")
    #print("***********")
    for i in best:
        #print(data[i])
        #print("length is ")
        #print(len(set([w for w in word_tokenize(data[i]) if w not in stopwordlist])))
        #print("list is ")
        #print(set([w for w in word_tokenize(data[i]) if w not in stopwordlist]))
        #print("length of the sentence")
        #print(len(data[i]))
        #print("*********")
        if len(set([w for w in word_tokenize(result) if w not in stopwordlist])) < len(set([w for w in word_tokenize(data[i]) if w not in stopwordlist])):
           result=data[i]
        elif len(result)<len(data[i]):
           result=data[i]
    print("high information")
    #print(data[max(dicti.items(), key=operator.itemgetter(1))[0]])
    #return data[max(dicti.items(), key=operator.itemgetter(1))[0]]
    return result
#search("hello world")
