# COMP551-Miniproject2
This is a private project for COMP551 miniproject2. This README is written by markdown and you may find [an instruction about how to use markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

## Important Dates
**Febuary 21, 2019** - Due date of this project  
...  

## Checklist Before Start
1) Read [project information](https://www.cs.mcgill.ca/~wlh/comp551/files/miniproject2_spec.pdf).  
2) Register [the Kaggle competition](https://www.kaggle.com/t/b95c2a432a9445d6a01a7a95d51d1dd5) using **McGill email**.  
3) Register Group on MyCourse.  
4) The [dataset](https://www.kaggle.com/c/12888/download-all) could be downloaded here.  

## Working Together
1) Please update **any change** made (i.e. implement a new function) in this document.  
2) Please write comments for **any parts of codes** that may be confusing.  
3) Please provide an estimated date of finishing coding.  
4) Please explain **any tests** you run and its related result. It would be preferred if you could write some **report-level** sentences as explaination which could be used as parts of our writeup.  

## Tasks  
1) **Bernoulli Naive Bayes** (w/o any external library).  
2) **At least 2** out of 3 classifiers from the SciKit. i.e. suggestions: logistic regression, decision tree, or support vector machines  
3) **At least 2** different features extraction pipelines for processing the data.  
4) A model validation. i.e. K-fold cross validation  

## TODO
1) Group meeting: assign tasks to each member.  
2) Feature engineering: discuss what kind of features are we going to use.  

## Updates
**<Januare 6, 2019>** [Pengnan Fan](https://github.com/Catosine) creates this project page and implements function readTrainData and readTestData. 
> * **readTrainData(address:String):DataFrame**  
> This function takes a string **address** which indicates the address of your train data and will load comments and isPositive to a DataFrame.  
> * **readTestData(address:String):DataFrame**  
> This function takes a string **address** which indicates the address of your test data and will load comments and isPositive to a DataFrame. **Note: all isPositive is initialized as 0**  
> * **Learning set** 25000 in total  
> * **Test set** 25000 in total  
