# -*- coding:utf-8 -*-
# @Script: max_consecutive_ones.py
# @Author: Pradip Patil
# @Contact: @pradip__patil
# @Created: 2019-03-21 23:28:31
# @Last Modified By: Pradip Patil
# @Last Modified: 2019-03-21 23:45:09
# @Description: https://leetcode.com/problems/max-consecutive-ones/

'''
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max = k = 0
        for i in nums:
            if i == 1:
                k += 1
                if k > max:
                    max = k
            else:
                k = 0

        return max


if __name__ == "__main__":
    print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
    print(Solution().findMaxConsecutiveOnes([1, 1, 1, 1, 0, 1, 1, 1]))
