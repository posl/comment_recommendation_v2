def buildTree(inorder, postorder):
    """
    :type inorder: List[int]
    :type postorder: List[int]
    :rtype: TreeNode
    """
    def helper(inorder, postorder):
        if not inorder: return None
        root = TreeNode(postorder.pop())
        idx = inorder.index(root.val)
        root.right = helper(inorder[idx+1:], postorder)
        root.left = helper(inorder[:idx], postorder)
        return root
    return helper(inorder, postorder)

if __name__ == '__main__':
    buildTree()