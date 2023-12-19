def buildTree(inorder, postorder):
    if len(inorder) == 0:
        return None
    if len(inorder) == 1:
        return TreeNode(inorder[0])
    root = TreeNode(postorder[-1])
    mid = inorder.index(postorder[-1])
    root.left = buildTree(inorder[:mid], postorder[:mid])
    root.right = buildTree(inorder[mid+1:], postorder[mid:-1])
    return root

if __name__ == '__main__':
    buildTree()