def buildTree(inorder, postorder):
    if len(inorder) == 0:
        return None
    root = TreeNode(postorder[-1])
    root_index = inorder.index(postorder[-1])
    root.left = buildTree(inorder[:root_index], postorder[:root_index])
    root.right = buildTree(inorder[root_index+1:], postorder[root_index:-1])
    return root

if __name__ == '__main__':
    buildTree()