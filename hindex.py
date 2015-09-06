import pprint

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        #pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(citations)

        highest_score = 0; 
        scoresDict = {}

        # If there are 5 papers, say 2, 2, 3, 4, 5
        # Iterate through all papers from 1..5
        # 2 means  
        # scoresDict[1] + 1
        # scoresDict[2] + 1
        # 3 means
        # scoresDict[1] + 1
        # scoresDict[2] + 1
        # scoresDict[3] + 1
        # etc...then we iterate through all scoresDict high->low and find the highest one where index >= value


        #for num in range(len(citations), 0, -1):
        for num in range(len(citations)):
            for score in range(citations[num]+1):
                scorekey = str(score)
                try:
                    scoresDict[scorekey] += int(1)
                except KeyError:
                    scoresDict[scorekey] = int(1)
 
                #scoresDict[scorekey] = scoresDict[scorekey] + int(1)
                #print 'score ' + str(score) + ' got' + str(scoresDict[scorekey])


        for key, value in reversed(sorted(scoresDict.items())): 
            #print str(key) + ' has value ' + str(value)
            if (int(key) <= int(value)): 
                return key

        return 0
