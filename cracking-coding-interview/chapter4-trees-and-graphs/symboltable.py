"""
Naive implementation symbol table: Linked list
"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_node = None
 
class LinkedListDict:
    def __init__(self):
        self.first = None
        self.size = 0

    def put(self, key, value):
        """
        Either overwrites value for key or inserts a new
        node containing (key, value) pair
        """
        if self.first is None:
            self.first = Node(key, value)

        curr, found = self._getnode(key)
        
        if found:
            curr.value = value
        else:
            new = Node(key, value)
            curr.next_node = new
            self.size += 1
    
    def get(self, key):
        """
        Returns either the value if key is defined
        otherwise None
        """
        curr, found = self._getnode(key)
        if found:
            return curr.value
        else:
            return None

    def delete(self, key):
        if self.first.key == key:
            self.first = self.first.next_node

        before = self.first
        curr = self.first
        while curr is not None and curr.key != key:
            before = curr
            curr = curr.next_node

        if curr is None:
            return # Key not found
        else:
            before.next(curr.next_node)
            self.size -= 1

    def contains(self, key):
        return self._getnode(key)[1]

    def isEmpty(self):
        return self.first is None

    def size(self):
        return self.size

    def keys(self):
        curr = self.first
        while curr is not None:
            yield curr.key
            curr = curr.next_node

    def __str__(self):
        items = []
        curr = self.first
        while curr is not None:
            items.append((curr.key, curr.value))
            curr = curr.next_node

        return '{' + ','.join(f'{key}:{value}' for key, value in items) + '}'
        
    def _getnode(self, key):
        """
        Returns a tuple that containes:
        - (keynode, True) where keynode is the node matching the key
        - (lastnode, False) node w/key wasn't found and return last node
        """
        curr = self.first
        while curr.next_node is not None and curr.key != key:
            curr = curr.next_node
        return (curr, curr.key == key)


mydict = LinkedListDict()

mydict.put("hola", 3)
mydict.put("hey", 1)

print("contains hey ", mydict.contains("hey"))
print(mydict)


mydict.put("hola", 8)

print("override hola")
print(mydict)
