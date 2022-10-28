class Solution:
    def twoSum(self, nums1: list[int], target: int) -> list():
        nums = nums1.copy()
        lst_out = [-1,-1]
        nums.sort()
        icur =(1 + target // 2)
       # print (nums)
        for i in range(0, len(nums) -1):
            if nums[i] > icur:
                break
            for j in range(i + 1,len(nums)):
                if ((nums[i] + nums[j]) == target):
                    lst_out[0] = nums1.index(nums[i])
                    lst_out[1] = nums1.index(nums[j])
                    if nums[i] == nums[j]:
                        lst_out[1] = nums1[lst_out[0] +1:].index(nums[j]) +1 +lst_out[0]


        return lst_out

sol = Solution()

nums = [3,3]
target = 6
lst_out = sol.twoSum(nums, target)
#print(sol.twoSum(nums, target))
print(lst_out)