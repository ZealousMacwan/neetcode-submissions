class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = [0] * 26;

        for char in s:
            index = ord(char) - ord('a')
            counter[index] += 1
        
        for char in t:
            index = ord(char) - ord('a')
            if counter[index] == 0:
                return False
            counter[index] -= 1
        
        return all(count==0 for count in counter)