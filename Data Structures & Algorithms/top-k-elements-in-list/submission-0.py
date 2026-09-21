class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        integer = {} #set

        for num in nums:
            integer[num] = integer.get(num, 0) + 1
        
        res = sorted(integer, key=integer.get, reverse=True)
        return res[:k]