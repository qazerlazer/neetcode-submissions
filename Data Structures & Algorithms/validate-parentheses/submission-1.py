class Solution:
    def isValid(self, s: str) -> bool:

        seen = []
        for i in range (0, len(s)):
            if s[i] == '{' or s[i] == '(' or s[i] == '[':
                seen.append(s[i])
            elif s[i] == '}':
                if len(seen) == 0 or seen[-1] != '{':
                    return False
                else:
                    seen.pop()
            elif s[i] == ')':
                if len(seen) == 0 or seen[-1] != '(':
                    return False
                else:
                    seen.pop()
            elif s[i] == ']':
                if len(seen) == 0 or seen[-1] != '[':
                    return False
                else:
                    seen.pop()
        return len(seen) == 0

        