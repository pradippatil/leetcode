# -*- coding:utf-8 -*-
# @Script: reverse_string.py
# @Author: Pradip Patil
# @Contact: @pradip__patil
# @Created: 2019-03-20 22:48:07
# @Last Modified By: Pradip Patil
# @Last Modified: 2019-03-20 22:57:17
# @Description: https://leetcode.com/problems/reverse-string/

'''
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.


Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''


class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n//2):
            s[i], s[n-i-1] = s[n-i-1], s[i]


if __name__ == '__main__':
    s1 = ["h", "e", "l", "l", "o"]
    print('orginal: ', s1)
    Solution().reverseString(s1)
    print('reversed:', s1)

    s2 = ["H", "a", "n", "n", "a", "h"]
    print('orginal: ', s2)
    Solution().reverseString(s2)
    print('reversed:', s2)
