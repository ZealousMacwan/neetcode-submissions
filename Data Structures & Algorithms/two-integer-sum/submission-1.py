class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenList = list()
        for index, n in enumerate(nums):
            comp = target-n
            if comp in seenList:
                return [nums.index(comp), index]
            else:
                seenList.append(n)        