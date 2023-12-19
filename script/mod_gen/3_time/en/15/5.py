def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None
    root = TreeNode(postorder[-1])
    rootIndex = inorder.index(root.val)
    root.left = buildTree(inorder[:rootIndex], postorder[:rootIndex])
    root.right = buildTree(inorder[rootIndex + 1:], postorder[rootIndex:-1])
    return root

if __name__ == '__main__':
    buildTree()