def buildTree(inorder, postorder):
    if not inorder:
        return None
    val = postorder.pop()
    root = TreeNode(val)
    inorderIndex = inorder.index(val)
    root.right = buildTree(inorder[inorderIndex+1:], postorder)
    root.left = buildTree(inorder[:inorderIndex], postorder)
    return root

if __name__ == '__main__':
    buildTree()