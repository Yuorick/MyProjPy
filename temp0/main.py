def isBadVersion(i):
    if i >= 4:
        return True
    else:
        return False

class Solution(object):
    def firstBadVersion(self, n):
        n0 =1
        n1 = n
        while True:
            m = (n1 - n0)
            if 1 == m:
                return n0
            ncur = n0 +  m//2
            if isBadVersion(ncur):
                n1 = ncur
            else:
                n0 = ncur

solv = Solution()
irez = solv.firstBadVersion(5)
print(irez)