Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    if not inorder:
        return None
    root_val = postorder[-1]
    root = TreeNode(root_val)
    root_index = inorder.index(root_val)
    root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
    root.right = self.buildTree(inorder[root_index+1:], postorder[root_index:-1])
    return root

=======
Suggestion 2

def buildTree(inorder, postorder):
    if not inorder:
        return None
    root = TreeNode(postorder.pop())
    inorderIndex = inorder.index(root.val)
    root.right = buildTree(inorder[inorderIndex + 1:], postorder)
    root.left = buildTree(inorder[:inorderIndex], postorder)
    return root

=======
Suggestion 3

def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    if len(inorder) == 0:
        return None
    root = TreeNode(postorder[-1])
    mid = inorder.index(postorder[-1])
    root.left = self.buildTree(inorder[:mid], postorder[:mid])
    root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])
    return root

=======
Suggestion 4

def buildTree(inorder, postorder):
    if len(inorder) == 0:
        return None
    if len(inorder) == 1:
        return TreeNode(inorder[0])
    root = TreeNode(postorder[-1])
    for i in range(len(inorder)):
        if inorder[i] == postorder[-1]:
            break
    root.left = buildTree(inorder[:i], postorder[:i])
    root.right = buildTree(inorder[i+1:], postorder[i:-1])
    return root

=======
Suggestion 5

def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        i = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:i],postorder[:i])
        root.right = self.buildTree(inorder[i+1:],postorder[i:-1])
        return root

=======
Suggestion 6

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None
    root = TreeNode(postorder.pop())
    inorderIndex = inorder.index(root.val)
    root.right = buildTree(inorder[inorderIndex+1:], postorder)
    root.left = buildTree(inorder[:inorderIndex], postorder)
    return root

=======
Suggestion 7

def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    if inorder:
        root = TreeNode(postorder.pop())
        root_index = inorder.index(root.val)
        root.right = self.buildTree(inorder[root_index + 1:], postorder)
        root.left = self.buildTree(inorder[:root_index], postorder)
        return root

=======
Suggestion 8

def buildTree(inorder, postorder):
    if len(inorder) == 0:
        return None
    root = TreeNode(postorder[-1])
    index = inorder.index(postorder[-1])
    root.left = buildTree(inorder[:index], postorder[:index])
    root.right = buildTree(inorder[index+1:], postorder[index:-1])
    return root

=======
Suggestion 9

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
