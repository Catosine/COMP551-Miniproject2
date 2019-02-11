# COMP551-Miniproject2
This is a private project for COMP551 miniproject2. It will be public after due date. In this project, we are required to learn and predict the sentiment of IMDB comments using classification.

## Important Dates
**Febuary 10, 2019** - First draft codes  
**Febuary 17, 2019** - Optimization  
**Febuary 21, 2019** - Due date of this project  
...  

## Checklist Before Start
1) Read [project information](https://www.cs.mcgill.ca/~wlh/comp551/files/miniproject2_spec.pdf).  
2) Register [the Kaggle competition](https://www.kaggle.com/t/b95c2a432a9445d6a01a7a95d51d1dd5) using **McGill email**.  
3) Register **Group45** on MyCourse.  
4) The [dataset](https://www.kaggle.com/c/12888/download-all) could be downloaded here.  

## Working Together
1) Please update **any change** made (i.e. implement a new function) in this document.  
2) Please write comments for any parts of codes that may be **confusing**.  
3) Please provide an estimated date of finishing coding of your part.  
4) Please explain **any tests** you run and its related results. It would be preferred if you could write some **report-level** sentences as explaination which could be used as parts of our writeup.  

## Tasks  
1) **Bernoulli Naive Bayes** (w/o any external library).  
> * **Hint1** - Laplace smoothing is helpful.  
> * **Hint2** - Vocabulary could be chosen by your own. But justification is required as a proof.   
2) **At least 2** out of 3 classifiers from the SciKit. i.e. suggestions: logistic regression, decision tree, or support vector machines  
3) **At least 2** different features extraction pipelines for processing the data. i.e. using binary occurrences and tf-idf weighting.  
4) A model validation. i.e. K-fold cross validation  

## TODO (Last update: Januare 7, 2019)
1) Finish assigned hypothesis  

## Dataset  
> * **Learning set**  
>> **Size** - 25,000 of positive and negative comments  
>> **Validation set** - 5 sets of 5,000 elements by cross validation  
> * **Test set**
>> **Size** - 25,000 of comments  

## Features
1. **Basic**  
> * **Word frequency naive** - numerical: frequency of words
> * **Word frequency w/o stopwords** - numerical: frequency of words without stopwords
> * **Present of a Word** - numerical, categorical: {0 -> No present,1 -> present}  
> * **Vocabulary of 3-gram w/o stopwords** - numerical: frequency of a given phrase within the whole set
> * **Conditional possibilities**  

## Hypothesis  
1. **Bernouolli Naive Bayes** by Pengnan  
> This hypothesis uses the conditional possibilities of words in comments to estimate the possibility of one given comment is either positive or negative.  
2. **Support Vector Machine** by Sherry  
3. **Logistic Regression** by Kaylee  

## Updates
**<Januare 6, 2019>** [Pengnan Fan](https://github.com/Catosine) creates this project page and implements functions readTrainData and readTestData. 
> * **readTrainData(address:String):DataFrame**  
> This function takes a string **address** which indicates the address of your train data and will load comments and isPositive to a DataFrame.  
> * **readTestData(address:String):DataFrame**  
> This function takes a string **address** which indicates the address of your test data and will load comments and isPositive to a DataFrame. **Note: all isPositive is initialized as 0**  
> * **Learning set** 25,000 in total  
> * **Test set** 25,000 in total  

**<January 7, 2019>** [Pengnan Fan](https://github.com/Catosine) implements wordsFrequencyNaive and wordsFrequencyStopword
> * **wordsFrequencyNaive(dataSet:DataFrame)**  
> This function takes a DataFrame **dataSet** and calculate the naive word frequency  
> * **wordsFrequencyStopword(dataSet:DataFrame)**  
> This function takes a DataFrame **dataSet** and calculate the word frequency without stopwords  

**<January 9, 2019>** [Pengnan Fan](https://github.com/Catosine) adds a new way to load files.  
> * **sklearn.datasets.load_files(address:str)** - [Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_files.html)  
> Returned data structure:  
>> data -> list of comments in byte type. You may transfer it into normal str by using **.decode("utf-8")**  
>> target_names -> type  

**<January 10, 2019>** [Pengnan Fan](https://github.com/Catosine) implements numOfExistanceNaive and numOfExistanceStopword
> * **numOfExistanceNaive(dataset:Bunch)**  
> This function takes a Bunch **dataSet** and calculate the naive existance of words  
> * **numOfExistanceStopword(dataset:Bunch)**  
> This funciton takes a Bunch **dataSet** and calculate the existance of words without stopwords  

**<January 11, 2019>** [Pengnan Fan](https://github.com/Catosine) implements bernoulliNaiveBayes and evaluation
> * **bernoulliNaiveBayes(dataSet:Bunch, totalWordFreq:set, negWordFreq:set, posWordFreq:set, numOfExamples:list)**  
> This function takes a Bunch **dataSet** as learning set and uses three sets of **totalWordFreq**, **negWordFreq**, **posWordFreq** and a list **numOfExamples** to calculates related probabilities. Note: It is not completely corrent. Fix later today.  
> * **evaluation(dataSet:Bunch, prediction:list)**  
> This function takes a Bunch **dataSet** and a list **prediction** to generate a set containing true pos\true neg\false pos\false neg  
