class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        p1 = 0
        p2 = 0
        hashmap = {}
        hashmap[s[p1]] = 0
        count = 1
        m = 1

        while p2 < len(s) - 1:
            p2 += 1
            while s[p2] in hashmap:
                del hashmap[s[p1]]
                count -= 1
                p1 += 1
            hashmap[s[p2]] = 0

            count += 1
            if count > m:
               m = count
        return m
            
            
            




        

            

            


        