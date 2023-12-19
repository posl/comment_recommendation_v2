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

if __name__ == '__main__':
    buildTree()