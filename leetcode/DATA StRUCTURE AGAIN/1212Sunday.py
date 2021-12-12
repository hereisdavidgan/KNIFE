# 217. 存在重复元素
# 给定一个整数数组，判断是否存在重复元素。
# 如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false】
'''
# 方法一：set() 创建一个无序不重复的集合
nums = [1,2,3,1]
if len(set(nums)) != len(nums):
    print ('1')
# 方法二：传统办法先排序后比较
nums.sort()
for i in range(len(nums)-1):
    if nums[i] == nums[i+1]:
        print ('1')
print ('2')
'''


# 53. 最大子序和
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

nums = [-2,1,-3,4,-1,2,1,-5,4]
n = len(nums)
for i in range(1,n):
    if nums[i-1] > 0:
        nums[i] += nums [i-1]
print (max(nums))