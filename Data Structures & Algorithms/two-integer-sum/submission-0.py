class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp in visited:
                return [visited[comp], i]
            visited[n] = i
        return []