def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(postorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        index = inorder.index(root.val)
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])
        return root

if __name__ == '__main__':
    buildTree()