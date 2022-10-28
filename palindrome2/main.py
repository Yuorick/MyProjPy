class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        pstr = str()

        if len(s) ==0:
            return True
        for i in range (len(s)):
            if s[i].isalnum():
                lcur = s[i]
                #lcur = lcur.upper()
                lcur = lcur.lower()
                #lcur = lcur.swapcase()
                pstr += lcur

        if pstr == pstr[::-1]:
            return True
        return False




sol = Solution()
s = "0P"
brez = sol.isPalindrome(s)
print(brez)
