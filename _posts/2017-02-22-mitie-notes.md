---
layout: post
title: Read the source code of MITIE
---
## MITIE introduction
MITIE is an awesome tool for performing named entity recognition tasks. For example, you may use MITIE to extract person names, company names, date, amount and many more entities from a sentence. It has many features:

* State-of-the-art NER
    * comparable to Stanford NER tool
    * https://github.com/mit-nlp/MITIE/wiki/Evaluation
* Free and open
    * MITIE is licensed under the Boost Software License 
* Support many languages
    * English, Spanish..
    * You can train specific word embedding feature extractor like Chinese and Japanese
* C++ implementation with ports to R, C, Python, Java and NodeJs
    * C++ makes sure the training and recognition are fast
    * Community-developed ports make MITIE extensible
    * We use the Java port in production, which leads me to learn about SWIG

This article is going to introduce the core components in MITIE with source code references. There are two components involved in a typical machine learning system:

* Training - calculate "the weights" based on training data
* Recognition - predict new data using calculated weights 

The above two components also apply to MITIE. 


## Training

### Segmenter
The features used to train a segmenter are coming from a kind of word embedding based on "Eigenwords: Spectral Word Embeddings". Take note that this segmenter traning is using the word embedding of the neighbour words. 

The model used here is a structured SVM, which optimizes the weights of linking the ground true labels with the training data. Structured SVM is a typical model to resolve sequence labelling problems. Other models include structured perceptron CRF, HMM...

### Chunk Classifier
After getting chunks like [John Becker], [HBU], it is time a train a normal multi-class SVM classifier to assign "person" and "organization" to the correct data.

To train this chunk classifier, MITIE uses more features like word hashing, isCap, containNumber, containHypen...., which seeems to be more representative in terms of how the actual entity looks like. I think it makes sense.


## Recognition
After training is done, a sequence will first go through the segmenter to get chunks. Then applying the chunk classifier on chunks to get the entities you want. This step is pretty naive and fast.


