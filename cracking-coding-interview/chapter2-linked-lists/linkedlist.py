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


def copylist(node: Node) -> Node:
    if node is None:
        return None

    new_root = Node(node.value)

    curr_new = new_root

    curr_old = node
    curr_old = curr_old.next

    while curr_old is not None:
        curr_new.next = Node(curr_old.value)

        curr_old = curr_old.next
        curr_new = curr_new.next

    return new_root


assert Node.buildfrom([0, 1, 2]) == copylist(Node.buildfrom([0, 1, 2]))


"""
Merge two sorted linked lists
"""
def merge_sorted(root1: Node, root2: Node) -> Node:
    """
    Merge 2 sorted lists in non-decreasing order

    There are 2 approaches here: to either create a new singly linked list
    with the new values or to modify one of these linked list. Because I
    like referential transparency and I don't like modifying existing
    objects, let's create a new list :)
    Runtime: O(N + M)
    Memory: O(N + M)
    """

    if root1 is None and root2 is None:
        return None
    elif root1 is None:
        new_root = copylist(root2)
        return new_root
    elif root2 is None:
        new_root = copylist(root1)
        return new_root

    curr1 = root1
    curr2 = root2
    
    if curr1.value < curr2.value:
        new_root = Node(curr1.value)
        curr1 = curr1.next
    else:
        new_root = Node(curr2.value)
        curr2 = curr2.next

    curr_newlist = new_root
    while curr1 is not None and curr2 is not None:
        if curr1.value < curr2.value:
            curr_newlist.next = Node(curr1.value)
            curr1 = curr1.next
        else:
            curr_newlist.next = Node(curr2.value)
            curr2 = curr2.next
        curr_newlist = curr_newlist.next

    if curr1 is None and curr2 is None:
        return new_root
    elif curr1 is None:
        curr_newlist.next = copylist(curr2)
    else:
        curr_newlist.next = copylist(curr1)

    return new_root



assert Node.buildfrom([0, 3, 6, 9]) == merge_sorted(Node.buildfrom([0, 3, 6, 9]), None)


l1 = Node.buildfrom([0, 2, 4, 6, 8])
l2 = Node.buildfrom([-1, 1, 3, 5, 7])
assert Node.buildfrom([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8]) == merge_sorted(l1, l2)



"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

def hascycle(root: Node) -> bool:
    """
    Use the two pointer technique. If the list has no cycles, then nodes will never cross
    If they do cross, then there's a cycle in it
    """
    if root is None:
        return False

    turtle = root
    rabbit = root.next

    while turtle is not None and rabbit is not None:
        """
        Super important! We need to use is NOT equal!
        Why? Equal won't finish because it will always keep
        iterating in the loop! And what we really want to ask
        is if this node(rabbit) POINTS AT THE SAME OBJECT than turtle
        And the above is what IS is for :)
        """
        if turtle is rabbit:
            return True
        turtle = turtle.next
        rabbit = rabbit.next
        if rabbit is not None:
            rabbit = rabbit.next
        else:
            return False # If None, we reached the end of the list!

    return False


l1 = Node(3)
l1.next = Node(2)
l1.next.next = Node(0)
l1.next.next.next = Node(-4)
l1.next.next.next.next = l1.next # -4 points to 2

assert False == hascycle(Node.buildfrom([0, 1, 2]))

assert True == hascycle(l1)

l2 = Node(1)
l2.next = Node(2)
l2.next.next = l2

assert True == hascycle(l2)

assert False == hascycle(Node(1))
