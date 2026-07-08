class Solution:
    def romanToInt(self, s: str) -> int:     # s means string

        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for i in range(len(s)):
            # here
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]

        return result
    
s = input("Enter a Roman numeral: ")
object = Solution()
result = object.romanToInt(s)
print(f"The integer value of the Roman numeral {s} is: {result}")