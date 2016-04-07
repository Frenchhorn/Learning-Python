'''
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
'''
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = 3 ** (len(str(n)) * 3)
        #a = 3**100
        if n <= 0:
            return False
        else:
            return a % n == 0

if __name__ == '__main__':
    a = Solution()
    b = a.isPowerOfThree(3**10000)
    print(b)
