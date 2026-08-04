class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        
        if len(s) != len(t):
            return False
        
        for i in range(0, len(s)):
            if s[i] in hashmap1:
                hashmap1[s[i]] += 1
            else:
                hashmap1[s[i]] = 0
            
            if t[i] in hashmap2:
                hashmap2[t[i]] += 1
            else:
                hashmap2[t[i]] = 0


          
        
        return hashmap1 == hashmap2
        