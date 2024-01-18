Synthesizing 10/10 solutions

=======
Suggestion 1

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        root_index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        root.right = self.buildTree(inorder[root_index+1:], postorder[root_index:-1])
        return root

=======
Suggestion 2

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None

        val = postorder.pop()
        root = TreeNode(val)
        idx = inorder.index(val)

        root.right = self.buildTree(inorder[idx+1:], postorder)
        root.left = self.buildTree(inorder[:idx], postorder)

        return root

=======
Suggestion 3

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        root_idx = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:root_idx], postorder[:root_idx])
        root.right = self.buildTree(inorder[root_idx + 1:], postorder[root_idx:-1])
        return root

=======
Suggestion 4

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        # inorder は 左 - 根 - 右
        # postorder は 左 - 右 - 根
        # なので、postorder の末尾が根になる
        # その根を inorder で探して、左右に分ける
        # 左右に分けたものを、それぞれ再帰的に処理する
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder.pop())
        root_index = inorder.index(root.val)
        root.right = self.buildTree(inorder[root_index+1:], postorder)
        root.left = self.buildTree(inorder[:root_index], postorder)
        return root

=======
Suggestion 5

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        
        root = TreeNode(postorder[-1])
        index = inorder.index(root.val)
        
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:len(postorder)-1])
        
        return root

=======
Suggestion 6

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        root = TreeNode(postorder.pop())
        rootIndex = inorder.index(root.val)
        root.right = self.buildTree(inorder[rootIndex+1:], postorder)
        root.left = self.buildTree(inorder[:rootIndex], postorder)
        return root

=======
Suggestion 7

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        if len(postorder) == 0:
            return None

        root = TreeNode(postorder[-1])
        root_index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        root.right = self.buildTree(inorder[root_index+1:], postorder[root_index:-1])
        return root

=======
Suggestion 8

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        if len(inorder) == 1:
            return root
        for i in range(len(inorder)):
            if inorder[i] == postorder[-1]:
                break
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        return root

=======
Suggestion 9

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        root = TreeNode(postorder.pop())
        root_index = inorder.index(root.val)
        root.right = self.buildTree(inorder[root_index + 1: ], postorder)
        root.left = self.buildTree(inorder[0: root_index], postorder)
        return root

=======
Suggestion 10

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        root = TreeNode(postorder.pop())
        inorderIndex = inorder.index(root.val)
        root.right = self.buildTree(inorder[inorderIndex+1:], postorder)
        root.left = self.buildTree(inorder[:inorderIndex], postorder)
        return root
