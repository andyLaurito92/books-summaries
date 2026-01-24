Incremental compilation is what C++, Java do, while live image interaction is what common lisp do. 

*Note* I thought Erlang also did the live image interaction. It seems that it doesn't. What it does is called
"Hot code Loading", that allows updating, replacing or adding code to a running system without stopping it.

- What's the difference then?
	- Between Java & Lisp -> Java doesn't gracefully allow the "Hot code swapping". If it does, it's only for restricted things (method, but not signature
	nor classes nor nothing that can modify an object size).
	- Between Erlang & Lisp -> Lisp updates the class definition, which all instances have a pointer at. So by updating this, when the instance tries to access it again, it finds out that the previous one was obsolete. 
	Erlan on the other hand, it preserves processes that had its previous code as they were, but it creates new proccesses (actors) with the new code. In this way, the system gracefully updates to the new code rather than changing on the fly.

Searching more about it, I found this super interesting project -> [Lisp flavoured erlang](https://lfe.io/). Summary: Lisp running on an erlang machine :O
