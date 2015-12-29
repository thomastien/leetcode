class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

	# Example,  1 9 3 6 2 7 5 4 0
	#  should return 8, because 9-1
	# 7 8 3 6 7 4 7 5 1
	#  should return 4, because 3-7 is the beat it can do

        min = 0
        best = 0
        count = 0

	for i in prices:
		count=count+1
		if (i < min or count==1):
			min = i
		difference = i-min
		#print (' ' + str(difference) + " for current val %s vs minimum %s" % (i, min))
		if difference > best:
			best = difference 

	return best;
