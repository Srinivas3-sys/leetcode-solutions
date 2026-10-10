class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map={}
        for i,x in enumerate(nums):
            if target-x in map:
                return [map[target-x],i]
            else:
                map[x]=i
