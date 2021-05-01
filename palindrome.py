class Solution:
    def isPalindrome(self, x: int):
       return False if x < 0 else x == int(str(x)[::-1])

 
