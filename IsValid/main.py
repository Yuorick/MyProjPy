class Solution(object):
    def isValid(self, s):
        nlen = len(s)
        nls = list([0] *nlen)
        for i in range(nlen):
            a = s[i]
            if s[i] == '(':
                nls[i] = 3
            if s[i] == ')':
                nls[i] = -3
            if s[i] == '[':
                nls[i] = 1
            if s[i] == ']':
                nls[i] = -1
            if s[i] == '{':
                nls[i] = 2
            if s[i] == '}':
                nls[i] = -2

        j0 = 0
        for i in range(0, nlen):
            if len(nls) == 0:
                return True
            breturn = True
            for j in range(j0, len(nls)):
                if nls[j] <= 0:
                    if j == 0:
                        return False
                    if nls[j] + nls[j -1] != 0:
                        return False
                    nls.pop(j )
                    nls.pop(j - 1)
                    breturn = False
                    j0 = max(0, j-2)
                    break
        if breturn == True:
            return False

solv = Solution()
s= "{[]}"
brez = solv.isValid(s)
print(brez)





