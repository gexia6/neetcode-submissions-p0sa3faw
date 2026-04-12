class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = [[]]
        n = len(nums)
        def dfs(start):
            for i in range(start, n):
                path.append(nums[i])
                res.append(path[:])
                dfs(i + 1)
                path.pop()
        dfs(0)
        return res





