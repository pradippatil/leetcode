# -*- coding:utf-8 -*-
# @Script: two_sum_2.py
# @Author: Pradip Patil
# @Contact: @pradip__patil
# @Created: 2019-03-21 21:59:19
# @Last Modified By: Pradip Patil
# @Last Modified: 2019-03-21 22:59:49
# @Description: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''


class Solution:
    def twoSum(self, numbers, target):
        end = len(numbers)
        for i in range(end):
            if i > 1 and numbers[i] == numbers[i-1]:
                continue
            start = i+1
            for j in range(start, end):
                if numbers[i] + numbers[j] == target:
                    return([i+1, j+1])
                elif numbers[i] + numbers[j] > target:
                    end = j
                    break


if __name__ == "__main__":
    print(Solution().twoSum([0, 1, 2, 3, 4, 5, 7, 10, 11], 9))
    print(Solution().twoSum([2, 7, 11, 15], 9))
