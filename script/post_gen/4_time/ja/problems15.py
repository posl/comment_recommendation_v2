Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        return self.helper(inorder, postorder)

=======
Suggestion 2

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        if len(postorder) == 0:
            return None

        root = TreeNode()
        root.val = postorder[-1]

        if len(postorder) == 1:
            return root

        for i in range(len(inorder)):
            if inorder[i] == postorder[-1]:
                break

        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])

        return root

=======
Suggestion 3

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        root_val = postorder[-1]
        root = TreeNode(root_val)
        mid = inorder.index(root_val)
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid + 1:], postorder[mid:-1])
        return root

=======
Suggestion 4

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None

        root_val = postorder[-1]
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)

        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        root.right = self.buildTree(inorder[root_index+1:], postorder[root_index:-1])

        return root

=======
Suggestion 5

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        if len(postorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        i = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:i], postorder[:i])
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
        if not inorder:
            return None
        root = TreeNode(postorder.pop())
        inorderIndex = inorder.index(root.val)
        root.right = self.buildTree(inorder[inorderIndex + 1:], postorder)
        root.left = self.buildTree(inorder[:inorderIndex], postorder)
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
        root_val = postorder[-1]
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)
        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        root.right = self.buildTree(inorder[root_index + 1:], postorder[root_index:-1])
        return root

=======
Suggestion 8

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        # 二分木探索の行きがけ順の走査は、左→中→右の順番
        # 二分木探索の帰りがけ順の走査は、左→右→中の順番
        # 二分木探索の行きがけ順の走査のリストの先頭が二分木のルートの値になる
        # 二分木探索の帰りがけ順の走査のリストの末尾が二分木のルートの値になる
        # 二分木探索の行きがけ順の走査のリストの先頭から二分木のルートの値を探し、その値の左側が二分木の左側、右側が二分木の右側になる
        # 二分木探索の帰りがけ順の走査のリストの末尾から二分木のルートの値を探し、その値の左側が二分木の左側、右側が二分木の右側になる
        # 二分木探索の行きがけ順の走査のリストの先頭から二分木のルートの値を探し、その値の左側が二分木の左側、右側が二分木の右側になる
        # 二分木探索の帰りがけ順の走査のリストの末尾から二分木のルートの値を探し、その値の左側が二分木の左側、右側が二分木の右側になる
        # 二分木探索の行きがけ順の走査のリストの先頭から二分木のルートの値を探し、その値

=======
Suggestion 9

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        # inorderの中からpostorderの最後の要素を探し、そのindexをiとする
        # inorder[:i]を左の部分木、inorder[i+1:]を右の部分木とする
        # postorderの最後の要素は根になるので、TreeNodeを作成
        # 左の部分木と右の部分木について再帰的に処理
        if inorder == []:
            return None
        root = TreeNode(postorder[-1])
        i = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        return root
