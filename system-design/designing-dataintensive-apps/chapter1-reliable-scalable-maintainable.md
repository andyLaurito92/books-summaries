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


### Twitter case

You need to implement twitter! What do you think that your big problem will be?

Well, in terms of requriements:

*Functional Requirements*
- User can post a tweet
- User can read its home
- User can follow another user

==== not to consider for now ====

- User can sign up
- User can post images
- User can modify within a time period the message sent?

*Non functional requirements*

- The system should allow posting messages with a maximum of X characters
- They system should have a latency from posting a message to appearing on the home of followes of 1s
- The system should be able to handle throughput of 5.000 tweets writes per second per region
- The system should be able to hnadle throughput of 15.000 reads of homes per second


From the above non-functional requirements, what we can see is that reading is gonna be at least 3 orders of maginute
bigger than writing! So probably that's where we want to emphasize the performance of our system!


The design problem in twitter is the *fanout* of tweets! How can we handle that? 2 approaches:

1- DB approach: 
	- Just insert into a database your tweets when somebody writes
	- When reading, select * tweets from table where follower = I'm folowwing
	
2-Inbox approach:
	- Have some sort of cache/queue per user where you get your new tweet
	- This implies that every time you post a tweet, you need to write *followes time!! Can be a lot! BUT,
	because how our system works, we care more about reading that writing! So it might be something that 
	we can support


