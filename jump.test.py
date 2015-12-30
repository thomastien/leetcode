#!/usr/bin/python

from jump import Solution

answer = Solution()

# Should return T T T T T F T
print answer.canJump([5,9,3,2,1,0,2,3,3,1,0,0]) 
print answer.canJump([0]) 
print answer.canJump([2,0]) 
print answer.canJump([2,5,0,0]) 
print answer.canJump([2,3,1,1,4])
print answer.canJump([3,2,1,0,4])
print answer.canJump([3,0,8,2,0,0,1])
