---
layout: post
title: SVM with Kernels 
description: Examples on how to use general kernels as well as customized kernels
---
###RBF kernel to solve XOR Problem  
	import numpy as np
	from sklearn import svm

	X = np.array([[-1,1],[1,1],[1,-1],[-1,-1]])
	y = [1,-1,1,-1]
	
	#Train SVM
	clf = svm.SVC(kernel='rbf')
	clf.fit(X, y)
	
	#Predict
	print clf.predict([0.2,0.2])
	print clf.predict([-0.2,0.2])
	print clf.predict([-0.2,-0.2])
	print clf.predict([0.2,-0.2])

The output is shown as follows, and it is totally right.
 
	[-1]
	[1]
	[-1]
	[1]

###Custom Kernel: precomputed kernel matrix
There is a nice tutorial: [http://mi.eng.cam.ac.uk/~mjfg/local/4F10/lect8.pdf](http://mi.eng.cam.ac.uk/~mjfg/local/4F10/lect8.pdf)  

We go on try to resolve the above XOR problem. The first stuff we are supposed to do is to calculate the kernel matrix. Refer to the tutorial in page 23.

![Gram Matrix](images/MachineLearning/GramMatrix.png)  

Afterward, we use the above kernel matrix to train SVM:  

	import numpy as np
	from sklearn import svm

	X = np.array([[-1,1],[1,1],[1,-1],[-1,-1]])
	y = ['A','B','A','B']


	gram = np.array([[9,1,1,1],[1,9,1,1],[1,1,9,1],[1,1,1,9]])
	clf = svm.SVC(kernel='precomputed')
	clf.fit(gram, y)

	test1 = np.array([1,4,1,0]) #kernel matrix respect to [0.5 0.5]
	test2 = np.array([4,1,0,1]) #kernel matrix respect to [-0.5 0.5]
	test3 = np.array([1,0,1,4]) #kernel matrix respect to [-0.5 -0.5]
	test4 = np.array([0,1,4,1]) #kernel matrix respect to [0.5 -0.5]

	print clf.predict(test1)
	print clf.predict(test2)
	print clf.predict(test3)
	print clf.predict(test4)

Here is the output, and it is exactly what we want.
	
	['B']
	['A']
	['B']
	['A']

Note that when doing testing, __the kernel values between all training vectors and the test vectors must be provided__. For example, [0.5 0.5] is used to test this system, and its original label is 'B'. The first thing to do is to calculate the kernel matrix, and it is:  
	
	[1, 4, 1, 0]

The above item is then used for prediction, and the result is 'B'.