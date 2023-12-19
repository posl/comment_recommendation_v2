def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None
    root = TreeNode(postorder.pop())
    rootIndex = inorder.index(root.val)
    root.right = buildTree(inorder[rootIndex+1:], postorder)
    root.left = buildTree(inorder[:rootIndex], postorder)
    return root

if __name__ == '__main__':
    buildTree()