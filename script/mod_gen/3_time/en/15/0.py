def buildTree(inorder, postorder):
    """
    :type inorder: List[int]
    :type postorder: List[int]
    :rtype: TreeNode
    """
    def build_tree(inorder, postorder):
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder.pop())
        root_index = inorder.index(root.val)
        root.right = build_tree(inorder[root_index + 1:], postorder)
        root.left = build_tree(inorder[:root_index], postorder)
        return root
    return build_tree(inorder, postorder)

if __name__ == '__main__':
    buildTree()