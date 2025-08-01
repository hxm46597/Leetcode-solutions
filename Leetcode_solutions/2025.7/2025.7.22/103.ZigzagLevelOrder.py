# Definition for a binary tree node.
import collections
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def Build_Tree(level_list):
    if not level_list or level_list[0] is None:
        return None
    root = TreeNode(level_list[0])
    queue = collections.deque([root])
    i = 1

    while queue and i< len(level_list):
        current = queue.popleft()

        #leftnode
        if i < len(level_list) and level_list[i] is not None:
            current.left = TreeNode(level_list[i])
            queue.append(current.left)
        i += 1

        #rightnode
        if i < len(level_list) and level_list[i] is not None:
            current.right = TreeNode(level_list[i])
            queue.append(current.right)
        i += 1
    return root

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root : return []
        res , deque = [] , collections.deque([root])
        while deque:
            tmp = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res) % 2 == 0 : tmp.append(node.val)
                else: tmp.appendleft(node.val)
                if node.left : deque.append(node.left)
                if node.right : deque.append(node.right)
            res.append(list(tmp))
        return res

level_list = [3, 9, 20, None, None, 15, 7]
sol = Solution()
root = Build_Tree(level_list)
result = sol.zigzagLevelOrder(root)
print(result)