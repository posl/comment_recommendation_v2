Synthesizing 10/10 solutions

=======
Suggestion 1

def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    if len(postorder) == 0:
        return None
    if len(postorder) == 1:
        return TreeNode(postorder[0])
    root = TreeNode(postorder[len(postorder) - 1])
    index = inorder.index(postorder[len(postorder) - 1])
    root.left = self.buildTree(inorder[:index], postorder[:index])
    root.right = self.buildTree(inorder[index + 1:], postorder[index:len(postorder) - 1])
    return root

=======
Suggestion 2

def buildTree(inorder, postorder):
    """
    :type inorder: List[int]
    :type postorder: List[int]
    :rtype: TreeNode
    """

    if len(inorder) == 0:
        return None

    root = TreeNode(postorder[-1])

    if len(inorder) == 1:
        return root

    index = inorder.index(postorder[-1])

    root.left = buildTree(inorder[:index], postorder[:index])
    root.right = buildTree(inorder[index+1:], postorder[index:-1])

    return root

=======
Suggestion 3

def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    if not inorder or not postorder:
        return None
    root = TreeNode(postorder.pop())
    inorderIndex = inorder.index(root.val)
    root.right = self.buildTree(inorder[inorderIndex+1:], postorder)
    root.left = self.buildTree(inorder[:inorderIndex], postorder)
    return root

=======
Suggestion 4

def buildTree(inorder, postorder):
    if not inorder:
        return None
    val = postorder.pop()
    root = TreeNode(val)
    inorderIndex = inorder.index(val)
    root.right = buildTree(inorder[inorderIndex+1:], postorder)
    root.left = buildTree(inorder[:inorderIndex], postorder)
    return root

=======
Suggestion 5

def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    if inorder:
        idx = inorder.index(postorder.pop())
        root = TreeNode(inorder[idx])
        root.right = self.buildTree(inorder[idx+1:], postorder)
        root.left = self.buildTree(inorder[:idx], postorder)
        return root

=======
Suggestion 6

def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(postorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        index = inorder.index(root.val)
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])
        return root

=======
Suggestion 7

def buildTree(inorder, postorder):
    if len(inorder) == 0:
        return None
    root = TreeNode(postorder[-1])
    rootIndex = inorder.index(postorder[-1])
    root.left = buildTree(inorder[:rootIndex], postorder[:rootIndex])
    root.right = buildTree(inorder[rootIndex+1:], postorder[rootIndex:-1])
    return root

=======
Suggestion 8

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None
    root = TreeNode(postorder.pop())
    inorderIndex = inorder.index(root.val)
    root.right = buildTree(inorder[inorderIndex+1:], postorder)
    root.left = buildTree(inorder[:inorderIndex], postorder)
    return root

=======
Suggestion 9

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None
    root = TreeNode(postorder.pop())
    rootIndex = inorder.index(root.val)
    root.right = buildTree(inorder[rootIndex+1:], postorder)
    root.left = buildTree(inorder[:rootIndex], postorder)
    return root

=======
Suggestion 10

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
