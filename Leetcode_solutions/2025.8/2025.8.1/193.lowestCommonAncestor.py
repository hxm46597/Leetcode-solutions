# Definition for a binary tree node.
import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else: break
        return root

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

def tree_to_level_order(root):
    if not root:
        return []

    result = []
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()

    return result

sol = Solution()
level_list = [6,2,8,0,4,7,9,None,None,3,5]
root = Build_Tree(level_list)
p = root.left
q = root.right
res = sol.lowestCommonAncestor(root, p, q)
result = tree_to_level_order(res)
print(result)