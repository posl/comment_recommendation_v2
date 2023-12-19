def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            root = TreeNode(postorder.pop())
            root_index = inorder.index(root.val)
            root.right = self.buildTree(inorder[root_index+1:], postorder)
            root.left = self.buildTree(inorder[:root_index], postorder)
            return root

if __name__ == '__main__':
    buildTree()