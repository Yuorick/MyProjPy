class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lcur = nums[-1]
        ncur = 1
        nrez = 0
        for i in range(1, len(nums)):

            if nums[len(nums) -1 -i] == lcur:

                ncur = ncur +1
                if i == (len(nums) -1):
                    nrez += 1
                    k = len(nums) - (1 + i) - (ncur - 1)
                    for j in range(i - ncur +1):
                        nums[len(nums) +1 -i +  j] = nums[len(nums) +1 -i  + ncur]

                    return nrez
                continue
            else:
                 if ncur == 1:
                    lcur = nums[len(nums) -1 -i]
                    nrez += 1
                    continue
                 else:
                    nrez += 1
                    for j in range(len(nums) -(1 +i) - (ncur - 1)):
                        nums[i+2 + j] = nums[i +1 + ncur]
                    ncur = 1
                    lcur = nums[len(nums) - 1 - i]

        print(nums)
        return nrez

sol = Solution()
nums = [1,1,2]
nrerz = sol.removeDuplicates(nums)
print(str(nrerz))
print(nums)


