class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1

        while i < len(s) / 2 and i < len(s) - 1 and j > -1:
            print(i, j, s[i], s[j])
            if s[i].isalnum() and s[j].isalnum():
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            if not s[i].isalnum():
                i += 1
            if not s[j].isalnum():
                j -=1
                
        
        return True
        