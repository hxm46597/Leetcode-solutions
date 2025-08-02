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

