def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None
    root = TreeNode(postorder.pop())
    index = inorder.index(root.val)
    root.right = buildTree(inorder[index+1:], postorder)
    root.left = buildTree(inorder[:index], postorder)
    return root

if __name__ == '__main__':
    buildTree()