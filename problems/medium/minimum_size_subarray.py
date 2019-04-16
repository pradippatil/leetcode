# -*- coding:utf-8 -*-
# @Script: minimum_size_subarray.py
# @Author: Pradip Patil
# @Contact: @pradip__patil
# @Created: 2019-03-22 00:09:44
# @Last Modified By: Pradip Patil
# @Last Modified: 2019-03-25 22:30:19
# @Description:  https://leetcode.com/problems/minimum-size-subarray-sum/


'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray
of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).


HINT: watch Minimum Window Substring method: https://www.youtube.com/watch?v=eS6PZLjoaq8
'''


class Solution:
    def minSubArrayLen(self, s, nums):
        start = end = sum = 0
        min_len = float('inf')

        while (end < len(nums)):
            sum += nums[end]
            end += 1
            while(sum >= s):
                min_len = min(min_len, end - start)
                sum -= nums[start]
                start += 1

        if min_len == float('inf'):
            return 0
        return min_len


if __name__ == "__main__":
    print('solution:', Solution().minSubArrayLen(17, [2, 3, 1, 2, 4, 3]))
    print('solution:', Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    print('solution:', Solution().minSubArrayLen(1, [1]))
    print('solution:', Solution().minSubArrayLen(11, [1, 2, 3, 4, 5]))
