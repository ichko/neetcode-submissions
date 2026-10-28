class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            freqs = {}
            for c in s:
                freqs.setdefault(c, 0)
                freqs[c] += 1
            ana_key = tuple(sorted([(k, v) for k, v in freqs.items()]))
            res.setdefault(ana_key, []).append(s)
        return list(res.values())