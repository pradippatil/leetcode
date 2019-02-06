# -*- coding:utf-8 -*-
# @Script: diagonal_traverse.py
# @Author: Pradip Patil
# @Contact: @pradip__patil
# @Created: 2019-02-05 23:31:22
# @Last Modified By: Pradip Patil
# @Last Modified: 2019-02-06 00:03:57
# @Description: https://leetcode.com/problems/diagonal-traverse/

"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.


Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

"""

from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, matrix):
        # Sum of indices for all values on diagonal remains same so group
        # matrix values in dictionary using key as sum of indices
        group = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                group[i+j+1].append(matrix[i][j])

        # Arrange grouped items in correct diagonal direction
        # Odd sum (key) will reverse direction
        result = []
        for k, v in group.items():
            if k % 2 == 0:
                result.extend(v)
            else:
                result.extend(v[::-1])
        return result


if __name__ == '__main__':
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().findDiagonalOrder(m))
