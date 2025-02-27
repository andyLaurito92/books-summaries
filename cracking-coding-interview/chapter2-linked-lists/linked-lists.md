A linked list is a sequence of Nodes. We generally represent it as follows:


``` 
class Node:
	@classmethod
	def buildfrom(a: list) -> Node:
		""" Useful method to remember 
		to build lists in a fast way"""
		if len(a) == 0:
			raise ValueError("Expected at least 1 element")
		
		root = Node(a[0])
		curr = root
		for x in a[1:]:
			curr.next = Node(x)
			curr = curr.next

		return root
		
	def __init__(self, value=None):
		self.value = value
		self.next = None
```

With the above code, you can easily insert assertions like follows in your code:

```python

assert Node.buildfrom([1, 2, 4, 5])  == deleteKthFromList(root, 3)

```

Remember that lists can be either single or doubly linked list

*Note* A list doesn't provide constant time to access a Kth element. For doing it, you will need O(K)


Why use it then if we have arrays? Because sometimes we just care about grabbing/removing the first element. 
For this, linked lists are great! (think about stacks and queues ;) )
I know, you can also do it with arrays, but remember that you do it in amortized time!


*Note* If we implement a linked list as a Node, then we might have a problem: How do we share that linked 
lists with other users? -> By sharing the root. Right, but what happens if the root changes? Then it means
that the users of our linked list will have lost the root because it changed!

How to solve the above? Wrap the root node in a linked list class. In this way, you always share the reference
for the linked list instance, and modify it's internal root Node in case something makes it change it

```
class LinkedList:
	def __init__(self):
		self.root = None
		
mylist = LinkedList()
mylist.root = Node(3)

# From now on, share mylist instead of mylist.root
```



