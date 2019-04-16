# -*- coding:utf-8 -*-
# @Script: rotate_array.py
# @Author: Pradip Patil
# @Contact: @pradip__patil
# @Created: 2019-04-01 21:36:57
# @Last Modified By: Pradip Patil
# @Last Modified: 2019-04-01 22:44:02
# @Description: https://leetcode.com/problems/rotate-array/

'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?

'''


class Solution:
    def reverse(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

    def rotate(self, nums, k):
        k %= len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)
        return nums

# Using builtins


class Solution_1:
    def rotate(self, nums, k):
        l = len(nums)
        k %= l
        nums[0:l] = nums[-k:] + nums[:-k]
        return nums


if __name__ == "__main__":
    print(Solution().rotate([-1, -100, 3, 99], 2))
    print(Solution_1().rotate([-1, -100, 3, 99], 2))
    print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3))
    print(Solution_1().rotate([1, 2, 3, 4, 5, 6, 7], 3))
