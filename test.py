#!/usr/bin/python

#from digit import Solution
#from anagram import Solution
from stack import Queue

answer = Queue()

answer.push(1)
answer.push(2)
print 'should be 1'
print answer.peek()
answer.pop()
print 'should be 2'
print answer.peek()
answer.empty()
answer.pop()
answer.pop()
print 'should be none'
print answer.peek()
