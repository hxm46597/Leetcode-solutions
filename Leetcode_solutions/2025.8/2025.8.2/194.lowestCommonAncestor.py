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
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right: return
        if not left: return right
        if not right: return left
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

sol = Solution()
Level_list = [3,5,1,6,2,0,8,None,None,7,4]
root = Build_Tree(Level_list)
p = 5
q = 1
res = sol.lowestCommonAncestor(root, p, q)
print(res)