class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts.setdefault(n, 0)
            counts[n] += 1
        freqs = list(counts.items())
        freqs_sorted = sorted(freqs, key=lambda x: -x[1])
        # print(freqs_sorted)
        kth_freq = freqs_sorted[k - 1][1]
        return [x[0] for x in freqs_sorted if x[1] >= kth_freq]