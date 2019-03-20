# -*- coding:utf-8 -*-
# @Script: longest_common_prefix.py
# @Author: Pradip Patil
# @Contact: @pradip__patil
# @Created: 2019-03-20 21:58:59
# @Last Modified By: Pradip Patil
# @Last Modified: 2019-03-20 22:14:02
# @Description: https://leetcode.com/problems/longest-common-prefix/

'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        smallest_length = min([len(s) for s in strs])
        string_to_compare = strs.pop()
        longest_common_prefix = ''
        for i in range(smallest_length):
            if not all([string_to_compare[i] == s[i] for s in strs]):
                break
            longest_common_prefix += string_to_compare[i]

        return longest_common_prefix


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
    print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
    print(Solution().longestCommonPrefix(["fl"]))
