class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        mapping = {
            'a': '0',
            'b': '1',
            'c': '2',
            'd': '3',
            'e': '4',
            'f': '5',
            'g': '6',
            'h': '7',
            'i': '8',
            'j': '9',
        }

        for k, v in mapping.items():
            firstWord = firstWord.replace(k, v)
            secondWord = secondWord.replace(k, v)
            targetWord = targetWord.replace(k, v)

        return int(firstWord) + int(secondWord) == int(targetWord)
