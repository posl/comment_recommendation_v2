from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
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
def levelOrder(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level_nodes = []
        for _ in range(level_size):
            node = queue.popleft()
            if node:
                level_nodes.append(node.val)
                # 子がいない場合にはNoneを追加する
                queue.append(node.left or None)
                queue.append(node.right or None)
            else:
                level_nodes.append(None)

        # 末尾のNoneを削除
        while level_nodes and level_nodes[-1] is None:
            level_nodes.pop()

        result.extend(level_nodes)
    return result
if __name__ == '__main__':
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))
    a = Solution()
    b = a.buildTree(inorder, postorder)
    print(levelOrder(b))