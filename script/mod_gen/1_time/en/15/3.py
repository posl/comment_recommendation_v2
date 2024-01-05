def buildTree(inorder, postorder):
    if len(inorder) == 0:
        return None
    root = TreeNode(postorder[-1])
    rootIndex = inorder.index(postorder[-1])
    root.left = buildTree(inorder[:rootIndex], postorder[:rootIndex])
    root.right = buildTree(inorder[rootIndex+1:], postorder[rootIndex:-1])
    return root

if __name__ == '__main__':
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))
    a = buildTree(inorder, postorder)
    print(a)