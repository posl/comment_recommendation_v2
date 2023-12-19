def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None
    root = TreeNode(postorder[-1])
    inorderIndex = inorder.index(root.val)
    root.left = buildTree(inorder[:inorderIndex], postorder[:inorderIndex])
    root.right = buildTree(inorder[inorderIndex+1:], postorder[inorderIndex:-1])
    return root

if __name__ == '__main__':
    buildTree()