'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

#用了两个循环
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        r = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        r.append(i)
                        r.append(j)
                        return r
'''
'''
#只用一个循环
class Solution(object):
    def twoSum(self, nums, target):
        temp = []
        for i in range(len(nums)):
            if nums[i] not in temp:
                temp.append(target-nums[i])
            else:
                return [temp.index(nums[i]),i]
'''
#用字典会更快
'''
class Solution(object):
    def twoSum(self, nums, target):
        index = {}
        for i, x in enumerate(nums):
            check = target - x
            if check in index:
                return [index[check], i]
            else:
                index[x] = i
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, n in enumerate(nums):
            if n in d:
                return [d[n], i]
            d[target - n] = i
            
if __name__ == '__main__':
    a = Solution()
    b = [1,2,3,4,5]
    c = 8
    print(a.twoSum(b,c))
