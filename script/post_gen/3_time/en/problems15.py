Synthesizing 10/10 solutions

=======
Suggestion 1

def buildTree(inorder, postorder):
    """
    :type inorder: List[int]
    :type postorder: List[int]
    :rtype: TreeNode
    """

    def build_tree(inorder, postorder):
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder.pop())
        root_index = inorder.index(root.val)
        root.right = build_tree(inorder[root_index + 1:], postorder)
        root.left = build_tree(inorder[:root_index], postorder)
        return root

    return build_tree(inorder, postorder)

=======
Suggestion 2

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None
    root = TreeNode(postorder.pop())
    index = inorder.index(root.val)
    root.right = buildTree(inorder[index+1:], postorder)
    root.left = buildTree(inorder[:index], postorder)
    return root

=======
Suggestion 3

def buildTree(inorder, postorder):
    if len(inorder) == 0:
        return None
    root = TreeNode(postorder[-1])
    index = inorder.index(postorder[-1])
    root.left = buildTree(inorder[:index], postorder[:index])
    root.right = buildTree(inorder[index+1:], postorder[index:-1])
    return root

=======
Suggestion 4

def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            root = TreeNode(postorder.pop())
            root_index = inorder.index(root.val)
            root.right = self.buildTree(inorder[root_index+1:], postorder)
            root.left = self.buildTree(inorder[:root_index], postorder)
            return root

=======
Suggestion 5

def buildTree(inorder, postorder):
    if len(inorder) == 0:
        return None
    root = TreeNode(postorder[-1])
    root_index = inorder.index(postorder[-1])
    root.left = buildTree(inorder[:root_index], postorder[:root_index])
    root.right = buildTree(inorder[root_index+1:], postorder[root_index:-1])
    return root

=======
Suggestion 6

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None

    root = TreeNode(postorder[-1])
    rootIndex = inorder.index(root.val)
    root.left = buildTree(inorder[:rootIndex], postorder[:rootIndex])
    root.right = buildTree(inorder[rootIndex + 1:], postorder[rootIndex:-1])

    return root

=======
Suggestion 7

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None
    root = TreeNode(postorder[-1])
    inorderIndex = inorder.index(root.val)
    root.left = buildTree(inorder[:inorderIndex], postorder[:inorderIndex])
    root.right = buildTree(inorder[inorderIndex+1:], postorder[inorderIndex:-1])
    return root

=======
Suggestion 8

def buildTree(inorder, postorder):
    if len(inorder) == 0:
        return None
    root = TreeNode(postorder[-1])
    index = inorder.index(root.val)
    root.left = buildTree(inorder[:index], postorder[:index])
    root.right = buildTree(inorder[index+1:], postorder[index:-1])
    return root

=======
Suggestion 9

def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    if not inorder or not postorder:
        return None
    root = TreeNode(postorder[-1])
    index = inorder.index(root.val)
    root.left = self.buildTree(inorder[:index], postorder[:index])
    root.right = self.buildTree(inorder[index+1:], postorder[index:-1])
    return root

=======
Suggestion 10

def buildTree(inorder: List[int], postorder: List[int]) -> TreeNode:
    def buildTreeHelper(inorder, postorder, inStart, inEnd, postStart, postEnd):
        if inStart > inEnd or postStart > postEnd:
            return None
        root = TreeNode(postorder[postEnd])
        rootIndex = 0
        for i in range(inStart, inEnd+1):
            if inorder[i] == root.val:
                rootIndex = i
                break
        root.left = buildTreeHelper(inorder, postorder, inStart, rootIndex-1, postStart, postStart+rootIndex-inStart-1)
        root.right = buildTreeHelper(inorder, postorder, rootIndex+1, inEnd, postStart+rootIndex-inStart, postEnd-1)
        return root
    return buildTreeHelper(inorder, postorder, 0, len(inorder)-1, 0, len(postorder)-1)
