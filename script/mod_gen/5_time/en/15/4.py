def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    if inorder:
        idx = inorder.index(postorder.pop())
        root = TreeNode(inorder[idx])
        root.right = self.buildTree(inorder[idx+1:], postorder)
        root.left = self.buildTree(inorder[:idx], postorder)
        return root

if __name__ == '__main__':
    buildTree()