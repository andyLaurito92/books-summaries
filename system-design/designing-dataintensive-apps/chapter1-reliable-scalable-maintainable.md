# Concepts

- Reliability: System should continue to work *correctly* even in the face of *adversity*

*What is correctly?* It means that it needs to fulfill the functional and non-functional requirement it was built for. 
*What is adversity?* Hardware or software failure, human error.

- Scalability: Growh in terms of data it receives. Question: If our system growths, what are our options to cope w/that growth?

- Maintainability: Keep working productively in the system even after many people work on them

## Questions

- How do you ensure that the data remains correct and compelte? Even when things go wrong internally?
- How do you provide consistently good performance to clients, even when parts of
your system are degraded?
- How do you scale to handle an increase in load?
- What does a good API for the service look like?

## Factors that influence design of a system

- Skills and experience of the people
- Legacy system depenedencies
- Timescale for delivery
- Organization's tolerance of different kinds of risk, regulatory constraints, etc.


## Scalability

In order to manage scalability, we need to understand how the current load of the system works. What does this mean?
It means that we need to understand the load parameters. What are these?

### Load parameters

These are parameters that can help us understand what is the growth that our system needs to cope with

- Requests x second
- Ratio of reads to writes in a DB
- Number of simultaneously active users
- Hit rate on a cache


From the above, think this: What will be the dominant factor? Think on how will you measure the aboves parameters!. 
For exapmle, thinking on perecentiles: What is the SLO for requests x second in terms of 95p? And 99p? 

*Remember* Think of perecentiles as "the x perecentile represents the x number of elements in my population that satisfies this requirement"

So for example if I say that 95p of latency in requests is < 10ms, I'm saying: "From 100 requests, 95 are < 10ms and only 5 > 10ms". 
