class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        pstout = ''
        quants = max(len(num1), len(num2))
        m = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(quants):
            n1 = 0
            n2 = 0
            try:
                n1 = int(num1[i])
            except:
                n1 =0
            try:
                n2 = int(num2[i])
            except:
                n2 =0
            n3 = n1 + n2 + m
            strcur = str(n3)
            if n3 < 10:
                m = 0
                pstout += strcur
            else:
                if i == (quants-1):
                    strcur = strcur[::-1]
                    pstout += strcur
                    break
                else:
                    pstout += strcur[1]
                    m = 1

        pstout = pstout[::-1]
        return pstout





num1 = "456"
num2 = "77"
solv = Solution()
num1 = solv.addStrings(num1, num2)
print(num1)


'''
c = 34343
pstr = bin(c)
print(pstr)
d = pow(2,32)
d = 2 *d
print(str(d))
'''