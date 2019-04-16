# -*- coding:utf-8 -*-
# @Script: remove_element.py
# @Author: Pradip Patil
# @Contact: @pradip__patil
# @Created: 2019-03-21 23:20:57
# @Last Modified By: Pradip Patil
# @Last Modified: 2019-03-21 23:23:51
# @Description: https://leetcode.com/problems/remove-element/

'''
iven an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
'''


class Solution:
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == "__main__":
    print(Solution().removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))
    print(Solution().removeElement(nums=[0], val=2))
    print(Solution().removeElement(nums=[], val=2))
