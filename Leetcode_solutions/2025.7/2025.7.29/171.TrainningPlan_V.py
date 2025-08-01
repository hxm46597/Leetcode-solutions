# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        A , B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A

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

def list_to_array(head):
    arr = []  # 初始化空数组
    current = head  # 从链表头开始
    while current:  # 当当前节点不为None时继续遍历
        arr.append(current.val)  # 将节点值添加到数组
        current = current.next  # 移动到下一个节点
    return arr  # 返回结果数组

sol = Solution()
level_list1 = [3,7,2,8,9,5,1]
level_list2 = [4,6,8,9,5,1]
l1 = Build_Linkedlist(level_list1)
l2 = Build_Linkedlist(level_list2)
res = sol.getIntersectionNode(l1,l2)
result = list_to_array(res)
print(result)