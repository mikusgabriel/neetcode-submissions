class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(s)
        s = re.sub(r'[^a-zA-Z0-9]', '', s)

        for i in range(0, len(s) // 2):
            first = s[i]
            second = s[len(s) - 1 - i]
            
            if first.lower() != second.lower():
                return False

        return True