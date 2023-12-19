def buildTree(inorder, postorder):
    """
    :type inorder: List[int]
    :type postorder: List[int]
    :rtype: TreeNode
    """
    if len(inorder) == 0:
        return None
    root = TreeNode(postorder[-1])
    if len(inorder) == 1:
        return root
    index = inorder.index(postorder[-1])
    root.left = buildTree(inorder[:index], postorder[:index])
    root.right = buildTree(inorder[index+1:], postorder[index:-1])
    return root

if __name__ == '__main__':
    buildTree()