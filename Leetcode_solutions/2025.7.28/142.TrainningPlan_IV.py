# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def trainningPlan(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = dum = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next , l1 = l1 , l1.next
            else:
                cur.next , l2 = l2 , l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dum.next

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
level_list1 = [1,2,4]
level_list2 = [1,3,4]
l1 = Build_Linkedlist(level_list1)
l2 = Build_Linkedlist(level_list2)
res = sol.trainningPlan(l1,l2)
result = list_to_array(res)
print(result)