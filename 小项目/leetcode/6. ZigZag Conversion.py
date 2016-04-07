'''
 The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        # calculate period
        p = 2*(numRows-1)

        res = [""] * numRows
        for i in range(len(s)):
            floor = i%p
            if floor >= p//2:
                floor = p - floor
            res[floor] += s[i]
        return "".join(res)

if __name__ == '__main__':
    a = Solution()
    b = 'PAYPALISHIRING'
    c = 4
    print(a.convert(b,c))
