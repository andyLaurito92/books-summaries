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
3. Back of the envelope estimation
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

