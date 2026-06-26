class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnter = Counter(tasks)
        max_v = max(cnter.values())
        reach_max_cnt = 0
        for v in cnter.values():
            if v == max_v:
                reach_max_cnt += 1
        return max(len(tasks), (max_v - 1) * (n + 1) + reach_max_cnt)