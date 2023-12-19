def buildTree(inorder, postorder):
    if inorder:
        ind = inorder.index(postorder.pop())
        root = TreeNode(inorder[ind])
        root.right = buildTree(inorder[ind+1:], postorder)
        root.left = buildTree(inorder[:ind], postorder)
        return root

if __name__ == '__main__':
    buildTree()