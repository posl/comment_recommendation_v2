def buildTree(inorder, postorder):
    if len(inorder) == 0:
        return None
    if len(inorder) == 1:
        return TreeNode(inorder[0])
    root = TreeNode(postorder[-1])
    root_index = inorder.index(postorder[-1])
    root.left = buildTree(inorder[:root_index], postorder[:root_index])
    root.right = buildTree(inorder[root_index+1:], postorder[root_index:-1])
    return root

if __name__ == '__main__':
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))
    a = buildTree(inorder, postorder)
    print(a)