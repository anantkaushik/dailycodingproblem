"""
Given a number in Roman numeral format, convert it to decimal.

The values of Roman numerals are as follows:
{
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.
For the input XIV, for instance, you should return 14.
"""
def romanToInt(s):
    dic={'I':1,'V':5,'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = prev = dic[s[-1]]
    for i in range(len(s)-2,-1,-1):
        val = dic[s[i]]
        if val < prev:
            num -= val
        else:
            num += val
        prev = val
    return num