def buildTree(inorder, postorder):
    if not postorder:
        return None
    root = TreeNode(postorder[-1])
    stack = [root]
    i = len(postorder) - 2
    j = len(inorder) - 1
    while i >= 0:
        node = TreeNode(postorder[i])
        temp = None
        while stack and stack[-1].val == inorder[j]:
            temp = stack.pop()
            j -= 1
        if temp:
            temp.left = node
        else:
            stack[-1].right = node
        stack.append(node)
        i -= 1
    return root

if __name__ == '__main__':
    buildTree()