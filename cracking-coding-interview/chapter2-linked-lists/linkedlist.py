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
        return root.next

    curr = root
    prev = curr
    while curr is not None:
        if curr.value == val:
            prev.next = curr.next
            return root
        prev = curr
        curr = curr.next
            

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


"""
Suppose that you had a linked list a1 -> a2 -> ... -> an -> b1 -> b2 -> ... -> bn, and you want
to rearrange it into a1 -> b1 -> a2 -> b2 -> ... -> an ->bn. You don't know the length of the linked list (but
you do know that the length is an even number)
"""

def rearrange(root: Node) -> Node:
    """
    Strong assumption: The list looks like this: a1 -> a2 -> ... -> an -> b1 -> b2 -> ... -> bn
    where b1 is the middle of the list and size is even
    """

    curr = root
    middle = root
    while middle is not None:
        curr = curr.next
        middle = middle.next.next # we can safely do this because there are even numbers

    # middle = a, curr = 1, prev_curr_next = 2, prev_middle_next = b
    # 1 -> 2 -> 3 -> a -> b -> c
    # curr.next = a, middle.next = 2  
    # 1 -> a -> 2 -> 3 ; b -> c
    # middle = b, curr = 2, prev_curr_next = 3, prev_middle_next = c
    # curr.next = b, middle.next = 3
    # 1 -> a -> 2 -> b -> 3 ; c
    # middle = c, curr = 3, prev_curr_next = a, prev_middle_next = None
    # curr.next = c, middle.next = a
    # 1 -> a -> 2 -> b -> 3 -> c -> a
    original_middle = curr

    middle = curr 
    curr = root
    prev_curr_next = curr.next
    prev_middle_next = middle.next
    while prev_middle_next is not None:
        prev_curr_next = curr.next
        prev_middle_next = middle.next

        curr.next = middle
        if prev_curr_next is not original_middle:
            # otherwise it's the last iteration
            middle.next = prev_curr_next

        curr = prev_curr_next
        middle = prev_middle_next

    return root



assert Node.buildfrom([1, 'a', 2, 'b', 3, 'c']) == rearrange(Node.buildfrom([1, 2, 3, 'a', 'b', 'c']))


assert Node.buildfrom(['a', 1, 'b', 2, 'c', 3, 'd', 4]) == rearrange(Node.buildfrom(['a', 'b', 'c', 'd', 1, 2, 3, 4]))
