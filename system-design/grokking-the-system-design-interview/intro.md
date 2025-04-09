# Grokking the system design interview - Author: ?

System design interviews are unstructured by nature -> This is totally the opposite to coding problems!


Let's define a template for this kind of interviews, like we do when we are 
implementing a dynamic programming solution that we use our STRBOT template

*Reminder about SRTBOT*
- Subproblem: Defines the subproblem space (If array, prefixes, sufixes, substrings)
This subproblem space defines the base case of the runtime that the algorithm will take
(substring is O(N^2), prefixes is O(N), and suffixes is O(N))
- Relation between subproblems: How do the above subproblems relate to solve the original problem?
- Topological order: What's the order in which we need to go through the subproblems?
- Basecase: Base or base cases to take into account
- Original: 
- Time: subproblem space * complexity of solving each subproblem

## Template

These are the templates to go through for a system design problem

1. Requirements Clarification
2. System interface definition
	2.1. Performance non-functional requriement
4. Defining data model
5. High-level design
6. Detailed design
7. Identifying and resolving bottlenecks

## Requirements clarification

In this step we ask questions that define the ontology of our system. Remember that the problem is a statement
(usually abstract) that needs to be reduced to multiple functional and non-functional requriements


*Key ideas:*
- Ask questions about the scope of the problem
- Clarify what parts of the system we will be focusing on

How do we ask good qeustions? 

By knowing in advanced the problems that might occurr in the problem statement :) This is nothing more than 
practise, practise and more practise!

### Example: Designing a twitter-like service, questions to ask:

- Will users of our service be able to post tweets and follow other people?
- Should we also design to create and display the user's timeline?
- Will tweets contain photos and videos?
- Are we focusing on the backend only or are we developing the foront-end too?
- Will users be able to search tweets?
- Do we need to display hot trending topics?
- Will there be any push notification for new tweets?


### Performance non-functional requirement

- Define what is the expected scale of the system (e.g., number of tweets, number
of tweets views, timele generation, etc)
- How much storage will we need? We will have different numbers if users can have 
photos and videos
- What network bandwith usage are we expecting?


## System interface definition

Define what APIs are expected from the system
- Will establish the contract
- Will ensure we haven't gotten any requirement wrong

Example for twitter-like service:

```
postTweet(user_id, tweet_data, tweet_location, user_location, timestamp, ...)
generateTimeline(user_id, current_time, user_location, ...)
markTweetFavorite(user_id, tweet_id, timestamp, ...)
```


## Define Data Model

Will clarify how data flow among different components of the system. Later, 
will guide us towards data partitioning and management

Things to take into consideration:
- Storage
- How we will transport data? 
- GDPR/GxP data
- Encryption at rest vs Encryption in transit
- Entities in the data model

Example for twitter-like service

```
User: userid, name, email, CreationData, lastlogin
Tweet: tweetid, content, tweetlocation, numberoflikes, timestamp
Userfollower: followed, followee
FavoriteTweets: userid, tweetid, timestamp
```

Type of database to use? Nosql? Sql? Cassandra? Mongodb? Graphdb? Mysql? Postgress?

## High-level design

Draw time!

For the twitter-like case: 

- Will we have more read or write traffic? What type of db is good for this?
- Where will we store the photos/videos?
- How we will organize our backend to handle different traffic? Will we think on monolithic or microservice app?
- What about the reverse-proxy? What kind of things do we need to take into account?
- Do we need a distributed file storage?
- What about monitoring/alerting?


## Detailed design

Dig deeper into two or three components based on the interviewer feedback!
The idea is to present different approaches, pros and cons, and explain 
why we choose one over the other

On the twitter-like service:

- How should we partition our data to distribute it to multiple databases? Should 
we try to store all the data of a user on the same db? Pros? Cons?
- How will we handle hot users who tweet a lot or follow lots of people?
- What kind of queries will we have? How do we optimize our db for the read case
of these?
- How much and at which layer should we introduce cache to speed things up?
- What components need better load balancing? Load balancing at which level?
