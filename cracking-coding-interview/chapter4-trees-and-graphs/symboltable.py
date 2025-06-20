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


class SortedListDict:
    def __init__(self):
        self.elements = []

    def put(self, key, value):
        self._insertionsort(key, value)

    def get(self, key):
        k = self._binary_search(key)

        if self.elements[k][0] == key:
            return self.elements[k][1]
        else:
            return None

    def delete(self, key):
        k = self._binary_search(key)
        if self.elements[k][0] != key:
            return
        else:
            while k < len(self.elements) - 1:
                self.elements[k] = self.elements[k + 1]
                k += 1
            del self.elements[len(self.elements) - 1]

    def contains(self, key):
        return self.get(key) is not None

    def isEmpty(self):
        return len(self.elements) == 0

    def size(self):
        return len(self.elements)

    def keys(self):
        for i in range(len(self.elements)):
            yield self.elements[i]

    def __str__(self):
        return str(self.elements)

    def _binary_search(self, key):
        """
        Returns the idx of key if found, otherwise return
        pos where the element should go
        """
        if len(self.elements) == 0:
            return 0

        print(self.elements)
        i = 0
        j = len(self.elements)
        while i < j:
            k = i + (j - i) // 2
            curr_key, _ = self.elements[k]
            if curr_key == key:
                return k
            elif key < curr_key:
                j = k
            else:
                i = k + 1
        return i

    def _insertionsort(self, key, value):
        i = self._binary_search(key)
        if i == 0:
            self.elements.insert(0, (key, value))
            return
        elif i >= len(self.elements):
            self.elements.append((key, value))
            return
        elif self.elements[i][0] == key:
            self.elements[i] = (key, value)
            return
       
        prev = self.elements[i]
        self.elements[i] = (key, value)
        i += 1
        while i < len(self.elements) - 1:
            self.elements[i] = prev
            prev = self.elements[i + 1]
        self.elements.append(prev)


class BSTNode:
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key
        self.value = value

class BSTDict:
    def __init__(self):
        self.node = None
        self.size = 0

    def put(self, key, value):
        if self.node is None:
            self.node = BSTNode(key, value)
            self.size += 1
            return

        curr = self.node
        while curr is not None:
            if curr.key == key:
                curr.value = value
                return
            elif key < curr.key:
                if curr.left is None:
                    curr.left = BSTNode(key, value)
                    self.size += 1
                    return
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = BSTNode(key, value)
                    self.size += 1
                    return
                else:
                    curr = curr.right

    # def delete(self, key):
    #     if self.node is None:
    #         return
    #     elif self.node.key == key:

    #         self.

    #     curr = self.node
    #     while curr is not None:
    #         curr.

    def get(self, key):
        curr = self.node
        while curr is not None and curr.key != key:
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def contains(self, key):
        return self.get(key) is not None

    def isEmpty(self):
        return self.size == 0

    def size(self):
        return self.size

    def keys(self):
        """
        Returns keys inorder, meaning that keys will
        be sorted in ascending order
        """
        mykeys = []
        self._inorder(self.node, lambda x: mykeys.append(x.key))
        for key in mykeys:
            yield key

    def items(self):
        res = []
        if self.node is None:
            return res

        self._inorder(self.node, lambda x: res.append((x.key, x.value)))
        return res

    def __str__(self):
        return '{' + ','.join(f'{key}:{value}' for key, value in self.items()) + '}'

    def _inorder(self, curr, visitfunc):
        if curr.left:
            self._inorder(curr.left, visitfunc)
        visitfunc(curr)
        if curr.right:
            self._inorder(curr.right, visitfunc)

implementations = [LinkedListDict(), BSTDict(), SortedListDict()]

for mydict in implementations: 
    print(f"Testing {type(mydict).__name__}")

    print()
    print("===============")
    print("Testing isEmpty")
    print("===============")
    print("isEmpty: ", mydict.isEmpty())
    print(mydict)
    print()

    print()
    print("===============")
    print("Putting elements")
    print("===============")
    print()

    mydict.put("hola", 3)
    mydict.put("hey", 1)

    print()
    print("===============")
    print("Testing contains")
    print("===============")
    print("contains hey ", mydict.contains("hey"))
    print(mydict)
    print()

    print()
    print("===============")
    print("Overriding hola")
    print("===============")
    mydict.put("hola", 8)
    print(mydict)
    print("===============")
    print()

    print()
    print("===============")
    print("Testing isEmpty")
    print("===============")
    print("isEmpty: ", mydict.isEmpty())
    print(mydict)
    print()
