---
layout: post
title: Earth Mover's distance in python
---

After digging through online resources, I am finally able to find two ways to calculate the Earth Mover's distance writing in Python. 


#### Interface between C implementation and Python modules
This approach is recommended for its speed. Basically, we add a file interface between the author's [C implementation](http://www.cs.duke.edu/%7Etomasi/software/emd.htm) and out own python modules. 

1. Update the author's code to fulfil our requirements. Example: [link](https://github.com/wihoho/Video-Recognition/tree/master/EarthMoverDistance%20SourceCode)
2. Call through python modules. Example: [link](https://github.com/wihoho/Video-Recognition/blob/master/calculateDistanceMatrix.py#L91)


#### Through Linear Programming Package (GLPK)


There are several steps to go.

1. Install GLPK (could be done through `brew`)
2. Install Pulp
3. Run the following script

<script src="https://gist.github.com/wihoho/6260278.js"></script>

The result is:

	160.542762808

