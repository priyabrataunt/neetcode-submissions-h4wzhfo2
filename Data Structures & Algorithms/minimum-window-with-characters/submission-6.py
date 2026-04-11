class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = {}
        for char in t:
            need[char] = 1 + need.get(char, 0)

        window = {}
        formed = 0
        required = len(need)

        left = 0
        result = ""
        min_len = float("inf")

        for right in range(len(s)):
            char = s[right]
            window[char] = 1 + window.get(char, 0)

            if char in need and window[char] == need[char]:
                formed += 1
            
            while formed == required:
                if(right - left + 1) < min_len:
                    min_len = right - left + 1
                    result = s[left:right+1]


                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    formed -= 1
                left += 1

        return result 