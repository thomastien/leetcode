#!/usr/bin/python


class Solution(object):
    # @return a boolean
    
    def _getSum(self,x):
        number_string = str(x)
        newsum = 0;
        for digit in number_string:
            newsum = newsum + int(digit)
        return newsum
         
    def addDigits(self, x):
        escape = 0;
        while x > 9:
            x = self._getSum(x)
            escape = escape+1
            if escape > 10:
                break 
        return x;
