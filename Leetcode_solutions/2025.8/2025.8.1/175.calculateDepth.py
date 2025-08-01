# Definition for a binary tree node.
import collections
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def calculateDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root: return 0
        return max(self.calculateDepth(root.left), self.calculateDepth(root.right)) + 1

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
level_list = [1,2,2,3,None,None,5,4,None,None,4]
root = Build_Tree(level_list)
res = sol.calculateDepth(root)
print(res)