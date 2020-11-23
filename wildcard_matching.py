class Solution:
    def isMatch2(self, s: str, p: str) -> bool:
        last_star_index = 0
        for i in range(len(p)):
            if p[i] != '*':
                break
            else:
                last_star_index = i 
        
           
        if last_star_index > 0 :
            p = p[last_star_index:]
        if s == '' and (p == '' or p == '*'):
            return True
        
        if len(p) == 0 or (len(s) == 0 and p != '*'):
            return False


        if s[0] == p[0] or p[0] == '?':
            return self.isMatch2(s[1:], p[1:])
        elif p[0] == '*':
            for i in range(len(s) + 1):
                if self.isMatch2(s[i:], p[1:]):
                    return True
                
            return False
        else:
            return False

    def isMatch(self, s: str, p: str) -> bool:
        len_p = len(p)
        len_s = len(s)

        dp = [[0] * (len_p+1) for _ in range(len_s+1)]

        dp[0][0] = 1

        for x in range(1, len_p+1):
            if p[x-1] == '*':
                dp[0][x] = dp[0][x-1]
        print(dp)
        for i in range(1, len_s+1):
            for j in range(1, len_p+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                print(dp)

        return bool(dp[-1][-1])

if __name__ == "__main__":
    sol = Solution()
    # print(sol.isMatch("aa", "*"))
    print(sol.isMatch( "abceb", "*a*b"))
    # print(sol.isMatch("babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb", "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a") )
    #print(sol.isMatch("bbaabbbbaaaabaabbbbabababaabaaaabaaabbaabaabaaabbabaabbbbbbbbbbaababbabaabbabaababbaaaabbbbaaaaaababbbbabbaababbabbabbababbbbabbbbaabaaabbaababbbaaaaababbbabbaaaaababbbaabbaabbbbbbbbbaababaababbababbabaa", "*b****abb***bbba**b*baaa****ba*ab***a*ab**a*a***aabbabb*bb**b***bbbbab****b*ba*baa*b*aa*b*b***a*bbab*" ))