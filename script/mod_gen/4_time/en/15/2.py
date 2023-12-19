def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    if len(inorder) == 0:
        return None
    root = TreeNode(postorder[-1])
    mid = inorder.index(postorder[-1])
    root.left = self.buildTree(inorder[:mid], postorder[:mid])
    root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])
    return root

if __name__ == '__main__':
    buildTree()