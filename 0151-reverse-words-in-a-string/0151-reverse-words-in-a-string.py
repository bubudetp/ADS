class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        symbol = " "
        result = ""
        reversed_sentence = ""
        last_char_seen = ""

        for i in range(len(s) - 1, -1, -1):
            if s[i] != symbol:
                result = s[i] + result
                last_char_seen = s[i]
            else:
                last_char_seen = s[i]

            if (last_char_seen == symbol or i == 0) and len(result) > 0:
                print("result", result)
                reversed_sentence = reversed_sentence + result + " "
                result = ""

        return reversed_sentence.strip()