class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if(len(s) < 3):
            return True
        if s == s[::-1]:
            return True

        s1 = s[:len(s) - 1]
        if s1 == s1[::-1]:
            return True
        s1 = s[1:]
        if s1 == s1[::-1]:
            return True
        for i in range(1, len(s)//2 +1):
            if s[i] != s[-1-i]:
                s2 = s[:i] + s[i + 1:]
                if s2 == s2[::-1]:
                    return True
                s2 = s[:-1-i] + s[-i:]
                if s2 == s2[::-1]:
                    return True
                return False
        return False

sol = Solution()
s ="deeee"
brez = sol.validPalindrome(s)
print(brez)