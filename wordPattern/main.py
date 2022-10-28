class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        ls = s.split()
        if len(ls) != len(pattern):
            return False

        word = ls[0]
        for j in range(len(pattern)):
            if word == ls[j]:
                if pattern[j] == pattern[0]:
                    ls[j] = pattern[0]
                else:
                    return False

        for i in range(1, len(pattern)):
            try:
                pattern[:i].index(pattern[i])
                if ls[i] == pattern[i]:
                    continue
                else:
                    return False
            except:
                word = ls[i]
                for j in range(i, len(pattern)):
                    if pattern[j] == pattern[i] and ls[j] == word:
                        ls[j] = pattern[i]

        st_erturn = str()
        for i in range(len(ls)):
            st_erturn += ls[i]
        if st_erturn == pattern:
            return True

        return False

solv = Solution()



pattern = "abba"
s  ="dog cat cat dog"
ls = solv.wordPattern(pattern,s)
print(ls)