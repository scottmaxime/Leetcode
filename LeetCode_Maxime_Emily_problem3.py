#Given a string s, find the length of the longest substring without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        listOfLetters = []
        dictionaryOfPreviousLetters = {}
        maximumLength = 0
        index = 0
        currentLength = 0
        debut = 1

        if s == "":
            return 0
        else:
            listOfLetters = list(s)
            lengthOfWord = len(s)
            for index in range(lengthOfWord):
                currentLetter = listOfLetters[index]
                if dictionaryOfPreviousLetters.get(currentLetter,0) == 0:
                    dictionaryOfPreviousLetters[currentLetter] = index + 1
                    currentLength += 1
                else:
                    if dictionaryOfPreviousLetters[currentLetter] >= debut:
                        if currentLength > maximumLength:
                            maximumLength = currentLength
                        
                        debut  = dictionaryOfPreviousLetters[currentLetter]
                        currentLength = index - debut + 1
                        dictionaryOfPreviousLetters[currentLetter] = index + 1
                    else:
                        dictionaryOfPreviousLetters[currentLetter] = index + 1
                        currentLength += 1
            if currentLength > maximumLength:
                maximumLength = currentLength
                        

            return maximumLength


