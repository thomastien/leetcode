#!/usr/bin/python

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # ok, basically as long as we don't get stuck at a zero, code can proceed
        permitted = 0

        if (len(nums) == 1):
            return True
        for i in xrange(1, len(nums)):
            if nums[i-1] == 0 and i >= permitted:
                return False 
            if i+nums[i-1] >= len(nums):
                return True 
            # Permitted is used to monitor if we should keep things goin
            #   this is need for cases like [3,0,8,2,0,0,1]
            if (i+nums[i-1] > permitted) :
                permitted = i+nums[i-1]
