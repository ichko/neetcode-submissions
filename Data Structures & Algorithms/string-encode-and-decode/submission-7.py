class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            n = len(s)
            out += f"{n}>{s}"
        return out

    def decode(self, s: str) -> List[str]:
        # print(s)
        i = 0
        buff = ""
        out = []
        while i < len(s):
            if s[i] == ">":
                # print(buff)
                size = int(buff)
                buff = ""
                str_now = s[i + 1:i+1+size]
                out.append(str_now)
                i += size + 1
            else:
                buff += s[i]
                i += 1
        
        return out
