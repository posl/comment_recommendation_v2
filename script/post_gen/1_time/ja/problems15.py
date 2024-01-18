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
        # inorderのrootのindexを取得
        root_index = inorder.index(root.val)
        # inorderのrootの左側をroot.leftとする
        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        # inorderのrootの右側をroot.rightとする
        root.right = self.buildTree(inorder[root_index+1:], postorder[root_index:])
        return root

=======
Suggestion 2

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
Suggestion 3

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None

        # postorderの最後の要素がroot
        root = TreeNode(postorder[-1])
        # inorderのrootのindexを取得
        root_index = inorder.index(root.val)

        # inorderをroot_indexで分割
        inorder_left = inorder[:root_index]
        inorder_right = inorder[root_index+1:]

        # postorderをinorderと同じ要素数になるように分割
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left):-1]

        # 再帰的に実行
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root

=======
Suggestion 4

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        def dfs(inorder, postorder):
            if inorder:
                val = postorder.pop()
                root = TreeNode(val)
                index = inorder.index(val)
                root.right = dfs(inorder[index+1:], postorder)
                root.left = dfs(inorder[:index], postorder)
                return root
        return dfs(inorder, postorder)

=======
Suggestion 5

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
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

        # postorderの最後の値が現在のノード
        val = postorder.pop()
        root = TreeNode(val)

        # inorderを分割する
        # 分割したinorderの左側が現在のノードの左側の子ノード
        # 分割したinorderの右側が現在のノードの右側の子ノード
        idx = inorder.index(val)
        root.right = self.buildTree(inorder[idx+1:], postorder)
        root.left = self.buildTree(inorder[:idx], postorder)

        return root

=======
Suggestion 7

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        if inorder == []:
            return None
        root = TreeNode(postorder[-1])
        root_idx = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:root_idx], postorder[:root_idx])
        root.right = self.buildTree(inorder[root_idx+1:], postorder[root_idx:-1])
        return root

=======
Suggestion 8

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        # 二分木探索の行きがけ順の走査と帰りがけ順の走査を与えられるので、二分木を構築する。
        # inorderは木探索の行きがけ順の走査であることが保証されているので、根ノードは必ず最後にある。
        # postorderは木探索の帰りがけ順の走査であることが保証されているので、根ノードは必ず最初にある。
        # したがって、postorderの最初の要素を根ノードとして、inorderの根ノードの位置を探索する。
        # この時、inorderの根ノードの左側が左部分木に、右側が右部分木になる。
        # この左部分木と右部分木に対して、それぞれ再帰的にこの処理を行えばよい。
        # ただし、inorderの根ノードの左側の部分木の要素数はpostorderの根ノードの左側の部分木の要素数と同じであることが保証されているので、
        # inorderの根ノードの左側の部分木の要素数を取得しておき、postorderの根ノードの左側の部分木の要素数として利用する。
        # また、inorderの根ノードの右側の部分木の要素数も同様である。
        # 以上より、再帰的にこの処理を行うことで、二分木を構築できる。
        # なお、postorderの根ノードの右側の部分木の要素数は、postorderの要素数から

=======
Suggestion 9

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        if len(postorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        if len(postorder) == 1:
            return root
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                break
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        return root

=======
Suggestion 10

def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
        # inorder: 左部分木のノードが並ぶ
        # postorder: 左部分木のノードが並ぶ

        # 1. postorderの最後の要素が根である
        # 2. inorderを根の左と右に分割する
        # 3. inorderの左部分木の要素数と同じ数だけpostorderの左部分木の要素が並ぶ
        # 4. inorderの右部分木の要素数と同じ数だけpostorderの右部分木の要素が並ぶ
        # 5. 分割した部分木に対して再帰的に処理を行う

        # inorderの要素数が0の場合はNoneを返す
        if len(inorder) == 0:
            return None

        # postorderの最後の要素が根である
        root = TreeNode(postorder[-1])

        # inorderを根の左と右に分割する
        # ここではinorderの要素を根の左部分木の要素と右部分木の要素に分割している
        # なお、inorderの要素はpostorderの要素と同じであるため、postorderの要素をinorderの要素で分割することもできる
        # 例えば、inorder = [9,3,15,20,7]、postorder = [9,15,7,20,3]の場合
        # inorderの要素で分割すると、左部分木の要素は[9]、右部分木の要素は[15,20,7]となる
        # postorderの要素で分割すると、左部分木の要素は[9,15,7]、右部分木の要素は[20,3]となる
        # いずれにせよ、inorderの要素とpostorderの要素は同じで
