# -*- coding:utf-8 -*-
# @Script: add_binary.py
# @Author: Pradip Patil
# @Contact: @pradip__patil
# @Created: 2019-03-19 00:06:31
# @Last Modified By: Pradip Patil
# @Last Modified: 2019-03-19 00:08:07
# @Description: https://leetcode.com/problems/add-binary/

'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))


if __name__ == '__main__':
    print(Solution().addBinary('11', '1'))
    print(Solution().addBinary('1010', '1011'))
