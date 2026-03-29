class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq_count = {}
        left = 0
        result = 0

        for right in range(len(s)):
            max_freq_count[s[right]] = 1 + max_freq_count.get(s[right], 0)
            window_size = right - left + 1
            if window_size - max(max_freq_count.values()) > k:
                max_freq_count[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
        return result
