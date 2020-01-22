# -*- coding: utf-8 -*-

"""Binary Tree Preorder Traversal

Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]

"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        nodes = []
        if root:
            nodes.append(root.val)
            if root.left is not None:
                nodes.extend(self.preorderTraversal(root.left))
            elif root.right is not None:
                nodes.extend(self.preorderTraversal(root.right))

        return nodes
