import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deduceTree(self, preorder, inorder):
        def recur(root, left, right):
            if left > right: return
            node = TreeNode(preorder[root])
            i = hmap[preorder[root]]
            node.left = recur(root + 1, left, i - 1)
            node.right = recur(i - left + root + 1, i + 1, right)
            return node

        hmap, preorder = {}, preorder
        for i in range(len(inorder)):
            hmap[inorder[i]] = i
        return recur(0, 0, len(inorder) - 1)

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
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
res = sol.deduceTree(preorder,inorder)
result = tree_to_level_order(res)
print(result)