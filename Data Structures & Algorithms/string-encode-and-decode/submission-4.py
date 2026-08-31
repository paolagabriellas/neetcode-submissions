class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded = encoded + str(len(s)) + "\n" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        splits = s.split("\n")
        length = int(splits[0])
        decoded = []
        for chunk in splits[1:]:
            word = chunk[:length]
            if chunk[length:]:
                length = int(chunk[length:])
            decoded.append(word)
        return decoded