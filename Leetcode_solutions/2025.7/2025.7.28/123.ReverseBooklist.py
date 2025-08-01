# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def Build_Linkedlist(Level_list):
    if not Level_list:
        return None

    head = ListNode(Level_list[0])
    current = head
    for i in Level_list[1:]:
        new_node = ListNode(i)
        current.next = new_node
        current = new_node
    return head
class Solution(object):
    def reverseBookList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]
sol = Solution()
Level_list = [3,6,4,1]
head = Build_Linkedlist(Level_list)
res = sol.reverseBookList(head)
print(res)