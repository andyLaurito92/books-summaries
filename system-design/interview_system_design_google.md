This is a summary for this [talk](https://www.youtube.com/watch?v=swfurPw8c6A)

What is a system engineer? 
- According to Wikipedia, focuses on designs and manage complex system over their lifecycle

From the above definition, we need to focus on 4 skills:
- Design
- Manage
- Complex system
- Lifecycle

## What does design mean?

To build systems from scratch. If they want to use pre-existing modules, they need to understand
how they work

Service level needs


## Manage?

Design a system for manageability. Build a system that can be mantained!

- Avoid unique point of failures
- Avoid bottlenecks

## Complex systems?

Scaling up can easily add complexity to the design

## Lifecycle

- Changing software versions
- Migration to new geographic location
- Replacement of failing services/hardware/etc


## Problem example

Design a system that copies a file into a destination :)

- 1st step: Do it
- 2ds step: Increase complexity: Larger file, not just one but many files, larger amount of targets
- 3rd step: Now the targets are at the moon! What do we need to take into consideration? Bandwith of the network? Size of the files?

### Bottlenecks

Identify the bottleneck. What is the bottleneck that is going to shape the design of your system?
Network? Disk I/O? Disk operations? Memory bandwith?

Usually can have many bottleneck dimensions!

Usual problem: Hardware looks pretty magical today! Nowadays, we can have super powerful machines that can have 1TB of memory and 
many CPUs :)


SSD vs harddrive, SSD had decreased a lot the amount of time we need to fetch data, write data, etc


### Functional vs non-functional requirements

Write down all of them


## Analogy of candidates and hiring bar

Candidates can be though as data points in a space. We have a hiring bar that divides the space between
hired and non-hire. *Goal of the interviewer:* Decrease the uncertainty of whether where does the candidate
lives according to the hiring bar

Initially, a candidate is a bar having a lot of error and then your job as interviewer is to decrease this error.

The above means: Be clear, conocise and precise!

## Hints

Candidates don't provide concrete estimates. How many machines? How many harddrives?
- Hint: _What needs to go in the purchase order to build your system?_

Don't clear boundaries between systems
- Hint: 3 teams of engineers that are going to design your system. How do we split work between them?

Resource estimation, don't drawn in a glass of water!
- Hint: 1 day, ~360.000.000 seconds

Magic bullets: Use some known technology that the candidate might not understad!
Example: I'm gonna use redis for this, I'm gonna use bittorrent for distributing files
- Hint: Okay, but how does it work? :)


SLO -> Service level objective

## Review on SLIs, SLOs, SLAs

*Main idea:* 
- Relaiability
- Availability
- Plan in case of failure

### Service Level Indicators (SLI)

*Summary:* The measure, just gathering data

When you read the word indicators, you are already defining that you need to measure! Metrics on their way :)

Usual indicators
- Metrics over time: Request latency x second / Failrues x Total Num Requests
	- Aggregated over time
	- Percentiles are useful here
	
*People involved:* SRE, Product developers

Example:

- "99th percentile latency of requests received in the past 5m < 300ms" Indicator 1
- "Errors total requests/total requests < 1%" Indicator 2
- 95% perecentile latency of homepage requests over past 5 minutes < 300ms

From the above indicators we build our SLO

But how? By aggregating all of the above results!

### Service Level Objectives (SLO)

*Summary:* The reading of the measure, aggregating indicators to define "good/bad".
Step were we add semantics to the data.From the indicators we define "What is good/bad" 

Now that we have defined our indicators, the questions would be: "How many times 
per AMOUNT OF TIME can we accept that we have Indicator 2 above the expected %? (errors/total requests)

AMOUNT OF TIME -> YEAR/MONTH/DAY

SLO define upper and lower bounds

*People involved:* SRE, Product developers

Example:
- 95% perecentile latency of homepage requests over past 5 minutes is met 99.9% over trailing year

#### Why don't we define the best SLO we can?

Because this depends entirely on the business and your stakeholders (think of APIs or
microservices that are consumed by other developers)!! 

If you define a super strict SLO, like Indicator 2 MUST BE between 0 <= sum(Indicator 2) <= 15, 
where sum represents the number of times the indicator failed, then meeting this goal could imply 
stopping development of features to meet the above SLO!!

If we are planning the SLO of the Broadcaster, fine. If we are planning as above the SLO
of a data pipeline for pharma, where they just need to present once a year this data, hmm..
Does it make sense?


### Service Level Agreements (SLA)

- It tells stakeholders: "This is what I gonna do if I don't meet the relaiabililty that I said
I was gonna meet"
- Focus more on business agreemnt & customer service provider
- Based on SLOs

Are then the same SLO and SLA?

NO! Your SLA should be more lenient (i.e. tolerant) than your SLO

*People involved:* Sales, end customers

Example:
- Service credit free if 95% perecentile latency of homepage requests over past 5 minutes doesn't meet 
99.5% over trailing year

### Summary

SLIs drive SLOs which inform SLAs

*Question:* Why don't we look for 100% relaiable/available? :)
*Answer:* Not real: Eitehr the cost or complexity of doing this is almost impossible to bare. However, 
it's true that we will try to narrow the distance between where we are and this ideal goal as much as 
possible.

