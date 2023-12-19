def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None
    root = TreeNode(postorder.pop())
    inorderIndex = inorder.index(root.val)
    root.right = buildTree(inorder[inorderIndex+1:], postorder)
    root.left = buildTree(inorder[:inorderIndex], postorder)
    return root
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
print(buildTree(inorder, postorder))
