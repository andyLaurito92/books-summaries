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
