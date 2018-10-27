---
layout: post
title: How to search logs through several clicks
---

After joining new company for 8 months, finally we have set up Elastic Search for our logs in new services. This is not
an easy step for me as a new joiner since there is already a log archived system running for many years.

Yes, it is always not easy to replace an old system especially when the old system is running "well". Everyone is getting
used to the old log system, and people is waiting for an hour to dig into the logs and use command line to search logs. Because 
people are getting used to the existing system, so there is less incentive to use new tools to improve the productivity.

But we have *several hundred hosts* running in production. 

## Shortcomings of old log system
Since I have been using Elastic Search for log analysis for some time, it is disaster for me to use old log archived system. The
shortcomings are listed below
* There is a time delay to populate logs (1 hour)
* Use specialized linux command to search for logs
* Need to search between request log and application log
* Slow
* Can only be done on an host
* Almost not possible to measure customer impact if something wrong is going on

During oncall, if there is some customer tickets requiring digging into logs, I am not willing to do so as a result. It is
also hard to image that such a big company is using such an old system to deal with logs. It is like 20 years ago.

## Use elastic search as solution 
It turns out to be super easy to set up Elastic Search in AWS, and stream logs directly from CloudWatch to Elastic Search. 
You actually only need to do the below steps.
1. [Load logs into CloudWatch using their agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-first-instance.html)
2. Set up Elastic Search using [AWS Elastic Search Service](https://aws.amazon.com/elasticsearch-service/)
3. [Stream CloudWatch into Elastic Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_ES_Stream.html)
4. Monitor the lambda function which does the streaming process
   * There is node js lambda setup automatically to stream

So even if you are new to these stuff, it takes at most 3 days to complete the first prototype. But of course, we still need
to spend time on maintaining and monitoring the Lambda function and Elastic Search service.  

## Callouts when using AWS Elastic Search to query logs
But there are still several holes involved during this process, and below are our walk-arounds.

#### Limit the concurrency in lambda in order to prevent overloading ES  

By default, the lambda concurrency is 1000, which means it is able to send 1000 requests to ES at the same time. Ignoring this
setting at the beginning actually overloads ES and we have several hours logs which are not indexed at all. So please start from
a small concurrency like 5, and try to adjust this number accordingly.

#### Index type shall be set to `cwl`
The node code running on Lambda sets the index name to be `log group name`. If there are multiple log groups streaming to ES,
only one group will be successful, the other group of logs will be discarded due to mismatch in the index name. 

It is easy to resolve this problem, we need to update the index name to a fixed string like `cwl` or any other string you like. 
In this case, ES will be able to index different types of logs with thanks to Dynamic Mapping. 

#### Make sure the logs are in proper format because by default `ignore_malformed = false`
Dynamic Mapping is not always a good thing. We are giving ES the absolute power to to define data type of each field. In our logs,
we sometimes see a field is `NaN` whereas it is detected to be `float` by ES. In such case, ES rejects to index such log and
returns an exception.

However, this is not what we want. Luckily there is a setting `ignore_malformed = true` which will continue to index the log
without indexing that malformed field. But is is not possible to adjust this setting once dynamic mapping has already been created.
So after realizing that we do not need such log, we actually filter such logs when we stream logs into ES.

To put it simple, we solve this issue by avoiding it.

####  set another lambda to delete old index 
Generally we are only interested in logs which are created within 30 days. To save cost, we are actually thinking to use another
lambda function to delete old indexes everyday. We have not implemented it yet. It looks like ES has a tool called curator which
can resolve this issue. But unfortunately, AWS Elastic Search is totally another world compared to Elastic's ES.

Let's index everything.