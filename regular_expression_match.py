
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #print(s, ", ", p)
        if s == p: 
            return True
        if (p == "" and s != "") or (s == "" and not p.endswith("*")) :
            return False 

        firstMatch = len(s) > 0 and (s[0] == p[0] or p[0] == '.')

        if len(p) > 1 and p[1] == '*':
            if firstMatch and self.isMatch(s[1:], p[0:]):
                return True
            else:
                return self.isMatch(s[0:], p[2:])
        elif firstMatch:
            return self.isMatch(s[1:], p[1:])
        else:
            return False

    def isMatch2(self, text:str , pattern: str) -> bool:
        memo = {}
        def dp(i:int, j:int) -> bool:
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans

            else:
                print("in memo", i, ", ", j)
            return memo[i, j]

        return dp(0, 0)

if __name__ == "__main__":
    s = Solution()
    print("False = {}".format(s.isMatch("a", ".*..a*")))
    print("True = {}".format(s.isMatch("", "c*c*")))
    print("True = {}".format(s.isMatch("bbbbafjdksjfkdsjafkldsjfkadsjfl", ".*a*a")))
    print("True = {}".format(s.isMatch("a", "ab*")))
    print("False = {}".format(s.isMatch("aa", "a")))
    print("True = {}".format(s.isMatch("aa", "a*")))
    print("True = {}".format(s.isMatch("ab", ".*")))
    print("True = {}".format(s.isMatch("ab", "..")))
    print("True = {}".format(s.isMatch("aab", "c*a*b")))
    print("False = {}".format(s.isMatch("mississippi", "mis*is*p*.")))
    print("True = {}".format(s.isMatch("", "")))



