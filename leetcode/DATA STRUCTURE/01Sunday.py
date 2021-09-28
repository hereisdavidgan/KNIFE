""" ## 217. 存在重复元素
给定一个整数数组，判断是否存在重复元素。
如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false """
""" 
class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]== nums[i+1]:
                return True
        return False
print(Solution.containsDuplicate(1,[1,1,2,3]))
print(Solution.containsDuplicate(1,[1,4,2,3]))
print(Solution.containsDuplicate(1,[1,1,2,2,3,3])) 
"""
""" ## 53. 最大子序和
给定一个整数数组 `nums` ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
> ```
> 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
> 输出：6
> 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
> `` """


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        single = 0
        maxs = nums[0]
        for i in range(len(nums)):
            single += nums[i]
            maxs = max(single,maxs)
            if single < 0:
                single = 0
        return maxs

## 动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1,n):
            if nums[i-1]>0:
                nums[i]+=nums[i-1]
        return max(nums)