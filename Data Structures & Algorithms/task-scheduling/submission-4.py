from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        frequencies = list(counts.values())
        maxFreq = max(frequencies)
        maxCounts = frequencies.count(maxFreq)
        ans = (maxFreq - 1) * (n + 1) + maxCounts
        return max(len(tasks), ans)