class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == None or x < 0:
            return False
        elif x < 10:
            return True
        elif x == self.reverse(x):
            return True
        else: 
            return False

    def reverse(self, x: int) -> bool:
        result = 0
        left = x
        while left > 0:
            left = int(left / 10)
            result = result * 10 + left % 10 
        return result

        
if __name__ == '__main__':
    sol = Solution()
    print("False == {}".format(sol.isPalindrome(100)))
    print("True == {}".format(sol.isPalindrome(121)))
    print("False == {}".format(sol.isPalindrome(None)))
    print("True == {}".format(sol.isPalindrome(1)))
    print("False == {}".format(sol.isPalindrome(-100)))
