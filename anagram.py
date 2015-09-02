import string

class Solution(object):
    # @return a boolean
    
    def isAnagram(self, first, second):
        #print 'Analyzing ' + first + ' vs ' + second + "\n"
        for char in first: 
            located = string.find(second, char)
            if located < 0:
                return False;
            second = string.replace(second, char, '', 1)
        #    print second
 
        #print first + "\n"
        #print second  + "\n---------------\n"
        
        if len(second) > 0:
            return False
        return True
