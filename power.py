
class Solution(object):
    # @return a boolean

    def isPowerofTwo(self,n):
        count = 0
        if n == 0: return False
        while (float(n%2) == 0 and count < 50):
            n = n / 2
            #print n
            count= count+1
        if n == 1:
            return True
        else: 
            return False
         
