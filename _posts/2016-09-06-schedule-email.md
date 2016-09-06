---
layout: post
title: Create schedule automatically using Machine Learning
---

My recent work is realted to extracting schedule information from emails automatically. We hope to be able to create schedules automatically based on
key information like date, time, subject and location.

There are mainly two steps involved.  

1. Perform text classification based the incoming email and determine whether this email is related to schedule or not.    
2. Perform named entity extraction on the emails filtered by step 1.

The above steps are pretty naive. However, we do not have any data. In order to start, we shall first prepare a dataset. To do so, we actually prepare our own dataset based on enron email dataset. Here are the steps on how we prepare our initial dataset.  

1. Index all enron emails into elasticsearch.  
2. User some keywords like "calendar" to filter emails.  
3. Label the emails produced by step 2 manually  

After the dataset is preapred, the next steps are pretty easy as we already have a great platform to perform NER and text classification. The entire
platform is primarily built on [MITIE](https://github.com/mit-nlp/MITIE). Frankly speaking, MITIE is the best NER library we find so far for its accuray and free license.

The work is still going on, and the results is so far so good. Hope that it could bring some convenience to the users.

