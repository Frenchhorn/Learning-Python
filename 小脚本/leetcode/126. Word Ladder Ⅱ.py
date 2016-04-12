
#Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

#Return
'''
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
'''
#Note:
'''
    All words have the same length.
    All words contain only lowercase alphabetic characters.
'''

#因为是用递归写的，不要用下面这个例子
'''
beginWord = "qa"
endWord = "sq"
wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
'''
class Solution(object):
    result = []
    re = []
    def findLadders(self, beginWord, endWord, wordList):
        self.re.append(beginWord)
        key = True
        for i in wordList:
            if self.ham(i, beginWord) == 1:
                if self.ham(i, endWord) == 1:
                    temp = self.re[:]
                    temp.append(i)
                    temp.append(endWord)
                    self.result.append(temp)
                l = wordList[:]
                del l[l.index(i)]
                self.findLadders(i, endWord, l)
                key = False
            if key == False:
                self.re.pop(-1)
                key = True
    def ham(self, word_1, word_2):
        h = 0
        for i, j in zip(word_1, word_2):
            if i != j:
                h += 1
        return h
                
if __name__ == '__main__':
    a = Solution()
    a.findLadders(beginWord, endWord, wordList)
    print(a.result)
            



        
        
            
