class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)
        visited = set()
        for r in range(n):
            if nums[r] not in visited:
                nums[l] = nums[r]
                l += 1
                visited.add(nums[r])
        return len(visited)