# -*- coding:utf-8 -*-
# @Script: implement-strstr.py
# @Author: Pradip Patil
# @Contact: @pradip__patil
# @Created: 2019-03-19 00:09:00
# @Last Modified By: Pradip Patil
# @Last Modified: 2019-03-19 00:50:23
# @Description: https://leetcode.com/problems/implement-strstr/

'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack) - (len(needle) - 1)):
            if needle == haystack[i:i+len(needle)]:
                return i

        return -1


if __name__ == '__main__':
    print(Solution().strStr(haystack="hello", needle="ll"))
    print(Solution().strStr(haystack="aaaaa", needle="bba"))
