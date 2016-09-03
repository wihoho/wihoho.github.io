---
layout: post
title: Python Notes
description: This article includes some highlights about python which I would like to emphasize
---

I do think writing blogs is a good way to conclude what you have learned so far. That's also why I decide to write this post to record some highlights about Python. Furthermore, it is also a good way to do revision, especially for someone like me who rarely do revision.


##Syntax  
`range(a,b)` returns the sequence of integers `a, a + 1,..., b - 1`  
  
`range(a,b,k)`: k is used as step value. For example: 

	for v in range(3,9,2):  
		print(v)  
	...  
	3  
	5  
	7


A function contains a header and body. The header begins with the `def` keyword, followed by the function's name and parameters, and ends with a colon. For example:  

	def min(num1, num2):
		if num1 < num2:
			return num1
		else:
			return num2

Passing arguments by reference values. The reference value of each argument is passed to the parameter each time when we invoke a function with arguments. This is referred to as `pass-by-value` in programming terminology.  

The contents of immutable objects cannot be changed. Whenever you assign a new number to a variable, Python creates a new object for the new number and assigns the reference of the new object to the variable. Notice that `number` and `strings` are known as immutable objects.

* For arguments of **immutable** objects such as numbers and strings, the original value of the object outside the function is not changed  

* For arguments of **mutable** objects, the original value of the object is changed if the contents of the object are changed inside the function   

Python `return` statement can return multiple values:  

	def sort(number1, number2):
    if number1 < number2:
        return number1, number2
    else:
        return number2,number1

	n1,n2 = sort(453,23)
	print("n1 is", n1)
	print("n2 is", n2)	  

`in` and `not in` are used to test whether a string is in another string or not.  
	
	>>> s1 = "Welcome"
	>>>"come" in s1
	True
	>>>"come" not in s1
	False

The `slicing operator` returns a slice of the list using the syntax `list[start : end]`.

The `repr(s)` function returns a raw string for s. 

	>>>s2 = "Hello \nWorld"
	>>>print(s2)
	Hello
	World
	>>>print(repr(s2))
	'Hello \nWorld'

##Basic Data Structure
* Tuple: use tuple for storing a fixed list of elements
* Set: a set for storing and quickly accessing non-duplicate elements
* Dictionary: store key/value pairs and access elements quickly using keys

 
For more samples, refer to [https://github.com/wihoho/LearningPython](https://github.com/wihoho/LearningPython)

