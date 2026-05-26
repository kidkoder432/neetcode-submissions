class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == [""]: return "[213]"
        elif strs == []: return "[342]"
        
        return "!@#$%eee".join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "[213]": return [""]
        if s == "[342]": return []
        return s.split("!@#$%eee")