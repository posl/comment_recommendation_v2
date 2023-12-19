Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None
    root = TreeNode(postorder[-1])
    root_index = inorder.index(postorder[-1])
    root.left = buildTree(inorder[:root_index], postorder[:root_index])
    root.right = buildTree(inorder[root_index+1:], postorder[root_index:-1])
    return root

=======
Suggestion 2

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

=======
Suggestion 3

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None
    root = TreeNode(postorder.pop())
    inorderIndex = inorder.index(root.val)
    root.right = buildTree(inorder[inorderIndex+1:], postorder)
    root.left = buildTree(inorder[:inorderIndex], postorder)
    return root

=======
Suggestion 4

def buildTree(inorder, postorder):
    if len(inorder) == 0:
        return None
    root = TreeNode(postorder[-1])
    rootIndex = inorder.index(postorder[-1])
    root.left = buildTree(inorder[:rootIndex], postorder[:rootIndex])
    root.right = buildTree(inorder[rootIndex+1:], postorder[rootIndex:-1])
    return root

=======
Suggestion 5

def buildTree(inorder, postorder):
    if len(inorder) == 0:
        return None
    if len(inorder) == 1:
        return TreeNode(inorder[0])
    else:
        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])
        return root

=======
Suggestion 6

def buildTree(inorder, postorder):
    if not inorder:
        return None
    root = TreeNode(postorder[-1])
    rootIndex = inorder.index(postorder[-1])
    root.left = buildTree(inorder[:rootIndex], postorder[:rootIndex])
    root.right = buildTree(inorder[rootIndex+1:], postorder[rootIndex:-1])
    return root

=======
Suggestion 7

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None
    root = TreeNode(postorder.pop())
    inorderIndex = inorder.index(root.val)
    root.right = buildTree(inorder[inorderIndex+1:], postorder)
    root.left = buildTree(inorder[:inorderIndex], postorder)
    return root

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
print(buildTree(inorder, postorder))

=======
Suggestion 8

def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    if not inorder or not postorder:
        return None
    root = TreeNode(postorder.pop())
    inorderIndex = inorder.index(root.val)
    root.right = self.buildTree(inorder[inorderIndex+1:], postorder)
    root.left = self.buildTree(inorder[:inorderIndex], postorder)
    return root
