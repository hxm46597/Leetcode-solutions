
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head: return
        hmap = {}
        cur = head
        while cur:
            hmap[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            hmap[cur].next = hmap.get(cur.next)
            hmap[cur].random = hmap.get(cur.random)
            cur = cur.next
        return hmap[head]

def build_random_list(arr):
    if not arr:
        return None

    nodes = []
    for item in arr:
        nodes.append(Node(item[0]))
    for i, item in enumerate(arr):
        if i < len(arr) - 1:
            nodes[i].next = nodes[i + 1]
        random_index = item[1]
        if random_index is not None:
            nodes[i].random = nodes[random_index]

    return nodes[0]


def random_list_to_array(head):
    if not head:
        return []
# 创建节点到索引的映射
    node_to_index = {}
    current = head
    index = 0
    while current:
        node_to_index[current] = index
        current = current.next
        index += 1
# 构建结果数组
    result = []
    current = head
    while current:
# 确定random索引
        random_index = None
        if current.random:
            random_index = node_to_index[current.random]

        result.append([current.val, random_index])
        current = current.next

    return result

Level_list = [[7,None],[13,0],[11,4],[10,2],[1,0]]
head = build_random_list(Level_list)
sol = Solution()
res = sol.copyRandomList(head)
result = random_list_to_array(res)
print(result)