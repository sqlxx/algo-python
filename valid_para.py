class Solution:
    def isValid(self, s: str) -> bool:
        bmap = {")":"(", "]":"[", "}":"{"}
        left = {"(", "[", "{"}
        right = {"}", "]", ")"}
        stack = []

        if not s:
            return True
        
        for i in range(len(s)):
            if s[i] in left:
                print("in left")
                stack.append(s[i])
            elif s[i] in right:
                if len(stack) == 0 or stack.pop() != bmap[s[i]]:
                    return False
        
        return len(stack) == 0
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))
