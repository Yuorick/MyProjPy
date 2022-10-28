class Solution(object):
    def platesBetweenCandles(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        def calc(pstr):
            try:
                ind0 = pstr.index('|*')
                try:
                    ind1 = pstr.rindex('*|')
                    if (ind1 < ind0):
                        return 0

                    q = pstr[ind0:(1 + ind1)].count('*')
                    return q

                except:
                    return 0
            except:
                return 0


        lsout = []
        slen = len(s)
        for i in range(0, len(queries)):

            ibegin = queries[i][0]
            iend = queries[i][1] + 1
            if iend > slen:
                icur = calc(s[ibegin:])
            else:
                icur = calc(s[ibegin:iend])


            lsout.append(icur)
        return lsout



s ="***|**|*****|**||**|*"

queries =[[1,17],[4,5],[14,17],[5,11],[15,16]]

solv = Solution()
lrez = solv.platesBetweenCandles(s, queries)
print(lrez)