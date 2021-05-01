class Solution:
    def reverse(self, x: int) -> int:
        if -2147483648 <= x <= 2147483647:
            if x < 0:
                x = abs(x)
                x = 0-Solution.reverse(x)
            else:
                x = Solution.reverse(x)
        return x if -2147483648 <= x <= 2147483647 else 0
    
    def reverse(x):
        test_num = 0
        while x:
            test_num = (test_num * 10) + (x % 10)
            x = x//10
        return test_num
        
