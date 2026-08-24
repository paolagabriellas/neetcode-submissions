class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string))
            encoded += ","
        encoded += "\n"
        combined = "".join(strs)
        encoded += combined
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        parts = s.split('\n')
        lengths = parts[0].split(",")[:-1]
        start = 0
        for length in lengths:
            string = parts[1][start:int(length)+start]
            start += int(length)
            decoded.append(string)

        return decoded            
