def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        i = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:i],postorder[:i])
        root.right = self.buildTree(inorder[i+1:],postorder[i:-1])
        return root

if __name__ == '__main__':
    buildTree()