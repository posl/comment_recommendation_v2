Synthesizing 10/10 solutions (Duplicates hidden)

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
        elif len(inorder) == 1:
            return TreeNode(inorder[0])
        else:
            root = TreeNode(postorder[-1])
            root_index = inorder.index(root.val)
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
        if inorder == []:
            return None
        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])
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
        val = postorder.pop()
        root = TreeNode(val)
        index = inorder.index(val)
        root.right = self.buildTree(inorder[index+1:], postorder)
        root.left = self.buildTree(inorder[:index], postorder)
        return root

=======
Suggestion 4

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        def buildTreeHelper(inorder_left, inorder_right):
            if inorder_left > inorder_right:
                return None

            # post_idxはポストオーダー配列の中で現在のサブツリーのルートを示す
            val = postorder.pop()
            root = TreeNode(val)

            # サブツリーを左右に分割
            # 分割した左右のツリーのサイズは同じ
            index = idx_map[val]

            # 再帰的に左右のサブツリーを構築
            root.right = buildTreeHelper(index + 1, inorder_right)
            root.left = buildTreeHelper(inorder_left, index - 1)
            return root

        # inorder配列の中の値とインデックスをマッピング
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return buildTreeHelper(0, len(inorder) - 1)

=======
Suggestion 5

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        if inorder:
            index = inorder.index(postorder.pop())
            node = TreeNode(inorder[index])
            node.right = self.buildTree(inorder[index+1:], postorder)
            node.left = self.buildTree(inorder[:index], postorder)
            return node

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
        
        # inorderの最後の要素がroot
        root = TreeNode(postorder[-1])
        # inorderの最後の要素のインデックスを取得
        root_idx = inorder.index(postorder[-1])
        
        # inorderの左側がleft subtree, 右側がright subtree
        root.left = self.buildTree(inorder[:root_idx], postorder[:root_idx])
        root.right = self.buildTree(inorder[root_idx+1:], postorder[root_idx:-1])
        
        return root

=======
Suggestion 7

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
        index = inorder.index(postorder[-1])
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])
        root.left = self.buildTree(inorder[:index], postorder[:index])
        return root

=======
Suggestion 9

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])

        return root
