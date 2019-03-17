# -*- coding:utf-8 -*-
# @Script: pascals_triangle.py
# @Author: Pradip Patil
# @Contact: @pradip__patil
# @Created: 2019-03-17 19:45:35
# @Last Modified By: Pradip Patil
# @Last Modified: 2019-03-17 20:20:52
# @Description: https://leetcode.com/problems/pascals-triangle/

'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        pascals_triangle = [[1], [1, 1]]
        for i in range(2, numRows):
            row = [1]
            for j in range(len(pascals_triangle[i-1])-1):
                row.append(pascals_triangle[i-1]
                           [j] + pascals_triangle[i-1][j+1])
            row.append(1)
            pascals_triangle.append(row)
        return pascals_triangle


if __name__ == '__main__':
    print(Solution().generate(0))
    print(Solution().generate(1))
    print(Solution().generate(2))
    print(Solution().generate(5))
