class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

         
        # Appending the 0 element: shouldn't influence the ultimate h-index
        # But is vital to handle scenarios such as
        # [0,1], [7,7,7,7,7,7,7] etc 
        # A) even # element cases
        # B) all elements are equal cases
        citations.append(0)
	citations.sort()
        citations.reverse()
        
        low, high = 1, len(citations) 

        #print citations

        #escape=0
        highest=0
        while high >= low:
            #print "boundary is now %s %s ..." % (low, high)
            n =  int( ((float(low)+high)/2))
            # remeber you are using an offset
            # so node #1 = [0] element, node #2 = [1]
            #print "  assessing node %s with value %s " % (str(n), str(citations[n-1]) )
            if citations[n-1] >= n:
                # Example, in [5, 4, 3, 2, 1]...first assessment would be does node 3 (3) >=3?
                # If yes, now need to go check node 4...so next time instead of scanning 12345...
                # 1) we first note current highest is 3
                # 2) make the next scan 345
                # 3) Also need to escape if it was already e.g. 45, k
                highest=n
                if low==n: return highest
                low = n    
            else:
                if high==n: return highest
                high = n

            ##escape +=1
            #if escape > 10 : return 99
            

        return 0
