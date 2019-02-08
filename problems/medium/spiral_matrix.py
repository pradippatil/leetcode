# -*- coding:utf-8 -*-
# @Script: spiral_matrix.py
# @Author: Pradip Patil
# @Contact: @pradip__patil
# @Created: 2019-02-05 23:31:22
# @Last Modified By: Pradip Patil
# @Last Modified: 2019-02-08 00:55:09
# @Description: https://leetcode.com/problems/spiral-matrix/

"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""


class Solution:
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        result = list()
        if not matrix:
            return result

        rows = len(matrix)
        cols = len(matrix[0])
        row_begin = 0
        row_end = rows - 1
        col_begin = 0
        col_end = cols - 1
        result = list()

        while len(result) < rows * cols:
            # traverse right
            if len(result) < rows * cols:
                for i in range(col_begin, col_end+1):
                    result.append(matrix[row_begin][i])
                row_begin += 1

            # traverse down
            if len(result) < rows * cols:
                for i in range(row_begin, row_end+1):
                    result.append(matrix[i][col_end])
                col_end -= 1

            # traverse left
            if len(result) < rows * cols:
                for i in range(col_end, col_begin-1, -1):
                    result.append(matrix[row_end][i])
                row_end -= 1

            # traverse up
            if len(result) < rows * cols:
                for i in range(row_end, row_begin-1, -1):
                    result.append(matrix[i][col_begin])
                col_begin += 1

        return result


if __name__ == '__main__':
    m = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print(Solution().spiralOrder(m))
