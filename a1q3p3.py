import os
import nltk
from nltk import *
import numpy
import sklearn
import random
import sklearn.metrics
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

from nltk.tokenize import word_tokenize
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords

def cleanUp(text, custom_stopwords=[]):
    # Initilaise Lemmatizer object:
    lemm = WordNetLemmatizer()
    
    # Load NLTK stopwords:
    my_stopwords = stopwords.words('english') + custom_stopwords
    
    clean_text = ''
    
    words = word_tokenize(text) # word_tokenize() takes care of stripping too.
    
    for word in words:
        w = lemm.lemmatize(word.lower())
        if w not in my_stopwords and len(w)>2:
            clean_text += w + ' '
    
    return clean_text

def load_dataset(file_path,file_type):
    array=['input']
    labeled=['input','label']
    with open(file_path,encoding="latin-1") as f:
        for line in f:
            if(file_type=="pos"):
                labeled.append([cleanUp(line),"pos"])
            elif(file_type=="neg"):
                labeled.append([cleanUp(line),"neg"])
            array.append(line)
    return array,labeled

pos_file,pos_data=load_dataset("rt-polaritydata/rt-polaritydata/rt-polarity.pos","pos")
neg_file,neg_data=load_dataset("rt-polaritydata/rt-polaritydata/rt-polarity.neg","neg")

dataset=pos_data+neg_data

train_set,test_set=sklearn.model_selection.train_test_split(dataset,train_size=0.8,test_size=0.2,shuffle=True)
x_train=[row[0] for row in train_set]
y_train=[row[1] for row in train_set]
x_test=[row[0] for row in test_set]
y_test=[row[1] for row in test_set]

vectorizer = CountVectorizer(ngram_range=(1, 2))
X = vectorizer.fit_transform(x_train)

from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer(use_idf=False)
X=tfidf_transformer.fit_transform(X)

def naiveBys(X,y_train,x_test,y_test):
    nb_detector = MultinomialNB()
    nb_detector.fit(X, y_train)
    X_test = vectorizer.transform(x_test)
    y_pred = nb_detector.predict(X_test)
    print ("NB Accuracy: ", sklearn.metrics.accuracy_score(y_test, y_pred))
    print (sklearn.metrics.confusion_matrix(y_test, y_pred, labels=["pos", "neg"]))

def LogReg(X,y_train,x_test,y_test):
    lg=LogisticRegression()
    lg.fit(X,y_train)
    X_test=vectorizer.transform(x_test)
    y_pred=lg.predict(X_test)
    print ("LR Accuracy: ", sklearn.metrics.accuracy_score(y_test, y_pred))
    print (sklearn.metrics.confusion_matrix(y_test, y_pred, labels=["pos", "neg"]))

def SVM(X,y_train,x_test,y_test):
    clf=SVC(kernel='linear')
    clf.fit(X,y_train)
    X_test=vectorizer.transform(x_test)
    y_pred=clf.predict(X_test)
    print ("SVM Accuracy: ", sklearn.metrics.accuracy_score(y_test, y_pred))
    print (sklearn.metrics.confusion_matrix(y_test, y_pred, labels=["pos", "neg"]))

naiveBys(X,y_train,x_test,y_test)
print("\n")
LogReg(X,y_train,x_test,y_test)
print("\n")
SVM(X,y_train,x_test,y_test)
print("\n")

