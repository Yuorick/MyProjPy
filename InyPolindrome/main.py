class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        pstr = str(x)
        ilen = len(pstr)
        n = ilen // 2
        breturn = True
        for i in range (n):
            if pstr[i] != pstr[ilen - 1 -i]:
                breturn = False
                break
        return breturn

    def isPalindrome1(self, x: int) -> bool:
        if x < 0:
            return False
       lst = list()

        return breturn

x  = 2,435,941
sol = Solution()
brez = True
brez = sol.isPalindrome(x)
print(brez)