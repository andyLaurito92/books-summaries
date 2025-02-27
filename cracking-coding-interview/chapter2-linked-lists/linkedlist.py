class Node:
    @classmethod
    def buildfrom(clss, a: list) -> 'Node':
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

    def __str__(self):
        elements = []
        curr = self
        while curr is not None:
            elements.append(str(curr.value))
            curr = curr.next

        return " -> ".join(elements)

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        else:
            return self.value == other.value and self.next == other.next
            


class LinkedList:
	def __init__(self):
		self.root = None
		
mylist = LinkedList()
mylist.root = Node(3)


def delete(root: Node, val) -> Node:
    """
    Deletes, if found, val from the singly linked list. If
    duplicates, it will remove just the first occurrence
    """

    if root is None:
        return root
    elif root.value == val:
        root.next = None
        return root.next

    curr = root
    prev = curr
    while curr is not None:
        if curr.value == val:
            prev.next = curr.next
            return root
            

def deletheKthNode(root: Node, k: int) -> Node:
    """
    DeletheKthNodes the kth element from the list. We start
    counting at 0-idx
    """
    if root is None:
        return root
    elif k == 0:
        return root.next

    curr = root
    prev = curr
    while k > 0 and curr is not None:
        prev = curr
        curr = curr.next
        k -= 1

    if curr is None:
        # k is greater than the size of the list
        return root
     
    prev.next = curr.next

    return root


assert deletheKthNode(Node.buildfrom(list(range(6))), 3) == Node.buildfrom([0, 1, 2, 4, 5])

assert deletheKthNode(Node.buildfrom(list(range(6))), 0) == Node.buildfrom([1, 2, 3, 4, 5]) 

assert deletheKthNode(Node.buildfrom(list(range(6))), 6) == Node.buildfrom([0, 1, 2, 3, 4, 5]) 

assert deletheKthNode(Node.buildfrom(list(range(6))), 5) == Node.buildfrom([0, 1, 2, 3, 4]) 


assert delete(Node.buildfrom(list(range(4))), 2) == Node.buildfrom([0, 1, 3])

assert delete(Node.buildfrom(list(range(4))), 0) == Node.buildfrom([1, 2, 3])
