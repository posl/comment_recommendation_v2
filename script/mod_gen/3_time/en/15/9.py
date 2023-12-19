def buildTree(inorder: List[int], postorder: List[int]) -> TreeNode:
    def buildTreeHelper(inorder, postorder, inStart, inEnd, postStart, postEnd):
        if inStart > inEnd or postStart > postEnd:
            return None
        root = TreeNode(postorder[postEnd])
        rootIndex = 0
        for i in range(inStart, inEnd+1):
            if inorder[i] == root.val:
                rootIndex = i
                break
        root.left = buildTreeHelper(inorder, postorder, inStart, rootIndex-1, postStart, postStart+rootIndex-inStart-1)
        root.right = buildTreeHelper(inorder, postorder, rootIndex+1, inEnd, postStart+rootIndex-inStart, postEnd-1)
        return root
    return buildTreeHelper(inorder, postorder, 0, len(inorder)-1, 0, len(postorder)-1)

if __name__ == '__main__':
    buildTree()