---
layout: post
title: Crawl Tumblr Blog
---

Sometimes you might want to get all images from the blog of tumblr you want. It does not necessarily be imgaes. They can be anything. Now we basically need a HTML parser to retrieve what we want. Here is a python implementation. Though you may use any languages, python is definitely an approprate tool to use here because of its simplicity and lots of libraries.  

Before we go into the topic, you need to install the following library  

* [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/)

Basically the logic is as follows:  

1. Read the front page
2. Parse the front page & store what you want
3. Go to the next page and repeat the above procedures
4. Keep doing so until the program can not read anything more

Here is the code:  
<script src="https://gist.github.com/wihoho/5972288.js"></script> 





