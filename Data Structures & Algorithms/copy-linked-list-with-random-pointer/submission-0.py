"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        Nodedict = {}
        ListPnter = head
        Nodedict[None] = None

        while ListPnter != None:
            Nodedict[ListPnter] = Node(ListPnter.val)
            ListPnter = ListPnter.next 

        ListPnter = head
        curr_node = Nodedict[ListPnter]
        while ListPnter != None:
            curr_node = Nodedict[ListPnter]
            curr_node.next = Nodedict[ListPnter.next]
            curr_node.random = Nodedict[ListPnter.random]
            ListPnter = ListPnter.next

        return Nodedict[head]