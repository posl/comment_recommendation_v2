def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    if len(inorder) == 0:
        return None
    if len(inorder) == 1:
        return TreeNode(inorder[0])
    root = TreeNode(postorder[-1])
    root_index = inorder.index(postorder[-1])
    root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
    root.right = self.buildTree(inorder[root_index+1:], postorder[root_index:-1])
    return root

if __name__ == '__main__':
    buildTree()