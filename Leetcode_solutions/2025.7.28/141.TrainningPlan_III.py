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

def list_to_array(head):
    arr = []  # 初始化空数组
    current = head  # 从链表头开始
    while current:  # 当当前节点不为None时继续遍历
        arr.append(current.val)  # 将节点值添加到数组
        current = current.next  # 移动到下一个节点
    return arr  # 返回结果数组
class Solution(object):
    def trainningPlan(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur , pre = head , None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
sol = Solution()
Level_list = [1,2,3,4,5]
head = Build_Linkedlist(Level_list)
res = sol.trainningPlan(head)
result = list_to_array(res)
print(result)