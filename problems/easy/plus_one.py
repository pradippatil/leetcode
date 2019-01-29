# -*- coding:utf-8 -*-
# @Script: plus_one.py
# @Author: Pradip Patil
# @Contact: @pradip__patil
# @Created: 2019-01-29 23:46:02
# @Last Modified By: Pradip Patil
# @Last Modified: 2019-01-29 23:47:13
# @Description: https://leetcode.com/problems/plus-one/

'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [int(i) for i in str(int(''.join([str(i) for i in digits]))+1)]
