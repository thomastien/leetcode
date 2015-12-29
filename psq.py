import math

class Solution(object):

    def _findCeiling(self,n):
        cuberoot = n ** (1.0/2)
        highestpossible = int(cuberoot)
        return highestpossible

 
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        print "assessing " + str(n)

        factors_found = 0
        counter = 0
 
        while (n > 0): 
            ceiling = self._findCeiling(n)
            print "ceiling %i" % ceiling
            n -= ceiling ** 2
            counter+=1
            #print "n is now at %i" % n
            if counter > 10:
                break
   

        return counter
	
        
