""" ## 1. 两数之和

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。 """

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         l2 = []
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i]+nums[j] == target:
#                     l2.append(i)
#                     l2.append(j)
#                     break
#         return(l2)

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashmap={}
#         for ind,num in enumerate(nums):
#             hashmap[num] = ind
#         for i,num in enumerate(nums):
#             j = hashmap.get(target - num)
#             if j is not None and i!=j:
#                 return [i,j]
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
for i in range(0, n): 
    nums1[i + m] = nums2[i]
    print(nums1)
    nums1.sort()
print(nums1)

nums1 = [0]
m = 0
nums2 = [1]
n = 1

nums3 = nums1[:m-1]+nums2[:n-1]
nums3.sort()
nums1 = nums3
print(nums1)