"""
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. 
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. 
You can assume the string to be decoded is valid.
"""
class stringCompression:
    def encode(self, s):
        result = []
        i = 0
        while i < len(s):
            char = s[i]
            charCount = 0
            while i < len(s) and s[i] == char:
                charCount += 1
                i += 1
            result.append(str(charCount))
            result.append(char)
        return "".join(result)
    
    def decode(self, s):
        result = []
        for i in range(0,len(s),2):
            countChar = int(s[i])
            result.append(s[i+1]*countChar)
        return "".join(result)
        
x = stringCompression()
print(x.encode("AAAABBBCCDAA"))
print(x.decode("4A3B2C1D2A"))