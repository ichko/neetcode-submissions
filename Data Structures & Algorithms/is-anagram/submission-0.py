class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        for c in s:
            freq_s.setdefault(c, 0)
            freq_s[c] += 1
        for c in t:
            if c in freq_s:
                freq_s[c] -= 1
            else:
                return False
            if freq_s[c] == 0:
                del freq_s[c]
        return len(freq_s) == 0
            