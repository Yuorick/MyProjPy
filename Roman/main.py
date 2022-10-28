class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]

        lsLetter = ['I', 'V', 'X','L', 'C', 'D', 'M']
        lsNum = [1, 5,10, 50, 100, 500, 1000]

        irez = 0
        icur = 0

        if s == '':
            return 0
        lsLetter.index(s[0])
        sc = s[0]
        iprev = lsLetter.index(s[0])
        irez = lsNum[iprev]
        if len(s) == 1:
            return irez

        for i in range(1, len(s)):
            icur = lsLetter.index(s[i])
            num = lsNum[icur]
            if icur < iprev:
                irez -= num
            else:
                irez += num
            iprev = icur
        return irez


sol = Solution()
s =  "MCMXCIV"
irez = sol.romanToInt(s)
print(str(irez))

