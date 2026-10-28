class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "[]"
        return ",1".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "[]":
            return []
        return s.split(",1")