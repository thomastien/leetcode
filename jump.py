#!/usr/bin/python

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        print(nums)
        if (len(nums) == 1):
            return True

        curindex = 1
        while (curindex < len(nums)):
            curindex += nums[curindex-1]
            print curindex
            if curindex > len(nums):
                return True
            if nums[curindex-1] == 0:
                return False
        return True
