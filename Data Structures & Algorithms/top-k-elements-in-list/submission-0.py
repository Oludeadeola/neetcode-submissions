from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: count frequency
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        
        # Step 2: convert to list of tuples (num, freq)
        items = list(freq_map.items())  # [(num, freq), ...]

        # Step 3: define function to get frequency
        def get_freq(item):
            return item[1]

        # Step 4: sort by frequency descending
        items.sort(key=get_freq, reverse=True)

        # Step 5: slice top k numbers
        top_k = [num for num, freq in items[:k]]

        return top_k

