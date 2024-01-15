#2つの整数配列 inorder と postorder が与えられ、ここでinorderは二分木探索の行きがけ順の走査、postorderは同じ木の帰りがけ順の走査である。
#この二分木を構築し、出力せよ。
#
#例 1：
#入力： inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
#出力： [3,9,20,null,null,15,7]
#
#例２：
#入力： inorder = [-1]、postorder = [-1]
#出力： [-1]
#
#制約：
#1 <= inorder.length <= 3000
#postorder.length == inorder.length
#-3000 <= inorder[i], postorder[i] <= 3000
#inorderとpostorderは一意な値で構成される。
#postorderの各値はinorderにも現れる。
#inorderは木探索の行きがけ順の走査であることが保証される。
#postorderは木探索の帰りがけ順の走査であることが保証される。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: list[int]
        :type postorder: list[int]
        :rtype: TreeNode
        """
