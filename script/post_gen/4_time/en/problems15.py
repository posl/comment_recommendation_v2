Synthesizing 10/10 solutions

=======
Suggestion 1

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder.pop())
        inorderIndex = inorder.index(root.val)
        
        root.right = self.buildTree(inorder[inorderIndex+1:], postorder)
        root.left = self.buildTree(inorder[:inorderIndex], postorder)
        
        return root

=======
Suggestion 2

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        stack = [root]
        inorderIndex = len(inorder) - 1
        for i in range(len(postorder) - 2, -1, -1):
            postorderVal = postorder[i]
            node = stack[-1]
            if node.val != inorder[inorderIndex]:
                node.right = TreeNode(postorderVal)
                stack.append(node.right)
            else:
                while stack and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex -= 1
                node.left = TreeNode(postorderVal)
                stack.append(node.left)
        return root

=======
Suggestion 3

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        inorderIndex = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:inorderIndex], postorder[:inorderIndex])
        root.right = self.buildTree(inorder[inorderIndex+1:], postorder[inorderIndex:-1])
        return root

=======
Suggestion 4

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        #if not inorder:
        #    return None
        #root = TreeNode(postorder[-1])
        #idx = inorder.index(postorder[-1])
        #root.left = self.buildTree(inorder[:idx], postorder[:idx])
        #root.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])
        #return root
        
        #if not inorder:
        #    return None
        #root = TreeNode(postorder[-1])
        #idx = inorder.index(postorder[-1])
        #root.left = self.buildTree(inorder[:idx], postorder[:idx])
        #root.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])
        #return root
        
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])
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
        i = inorder.index(root.val)
        root.left = self.buildTree(inorder[:i],postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        return root

=======
Suggestion 6

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder[-1])
        root_index = inorder.index(postorder[-1])
        
        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        root.right = self.buildTree(inorder[root_index + 1:], postorder[root_index:-1])
        
        return root

=======
Suggestion 7

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        rootIndex = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[0:rootIndex], postorder[0:rootIndex])
        root.right = self.buildTree(inorder[rootIndex+1:], postorder[rootIndex:-1])
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
        root_index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        root.right = self.buildTree(inorder[root_index+1:], postorder[root_index:-1])
        return root

=======
Suggestion 9

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        # inorder: left, root, right
        # postorder: left, right, root
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])
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
        root = TreeNode(postorder[-1])
        i = inorder.index(root.val)
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        root.left = self.buildTree(inorder[:i], postorder[:i])
        return root
