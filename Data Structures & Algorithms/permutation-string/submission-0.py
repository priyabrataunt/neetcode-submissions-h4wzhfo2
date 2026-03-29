class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap_s1 = {}
        hashmap_s2 = {}

        for char in s1:
            hashmap_s1[char] = 1 + hashmap_s1.get(char, 0)
        for char in s2[0:len(s1)]:
            hashmap_s2[char] = 1 + hashmap_s2.get(char, 0)

        if hashmap_s1 == hashmap_s2:
            return True
        
        for next_window in range(len(s1), len(s2)):
            hashmap_s2[s2[next_window]] = 1 + hashmap_s2.get(s2[next_window], 0)
            left = next_window - len(s1)
            hashmap_s2[s2[left]] -= 1
            if hashmap_s2[s2[left]] == 0:
                del hashmap_s2[s2[left]]
            if hashmap_s1 == hashmap_s2:
                return True
        return False
            