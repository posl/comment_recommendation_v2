def buildTree(inorder, postorder):
    if len(inorder) == 0:
        return None
    if len(inorder) == 1:
        return TreeNode(inorder[0])
    root = TreeNode(postorder[-1])
    for i in range(len(inorder)):
        if inorder[i] == postorder[-1]:
            break
    root.left = buildTree(inorder[:i], postorder[:i])
    root.right = buildTree(inorder[i+1:], postorder[i:-1])
    return root

if __name__ == '__main__':
    buildTree()