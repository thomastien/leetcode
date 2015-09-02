#!/usr/bin/python

#from digit import Solution
from anagram import Solution

answer = Solution()
print answer.isAnagram('foobar', 'raboof')
print answer.isAnagram('hello', 'world')
print answer.isAnagram('hehe', 'heh')
print answer.isAnagram('heh', 'hehe')
print answer.isAnagram('bluebells', 'bells')
print answer.isAnagram('able wasi', 'iwasable')
print answer.isAnagram('ablewasi', 'iwasable')
