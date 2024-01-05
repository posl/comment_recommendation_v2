def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None
    root = TreeNode(postorder.pop())
    inorderIndex = inorder.index(root.val)
    root.right = buildTree(inorder[inorderIndex+1:], postorder)
    root.left = buildTree(inorder[:inorderIndex], postorder)
    return root

if __name__ == '__main__':
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))
    a = buildTree(inorder, postorder)
    print(a)