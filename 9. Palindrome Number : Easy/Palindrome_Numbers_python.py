# With converting the int to str
class Solution:
    def isPalindrome(self, x: int) -> bool:
        word = str(x)
        reverse_word = ""

        for i in range(len(word)-1,-1,-1):
            reverse_word += word[i]

        if word == reverse_word:
            return True
        else:
            return

# Without converting the int to str
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         original = x
#         number = x
#         last_digit = 0
#         reverse = 0
        

#         while number > 0:
#             last_digit = number % 10
#             reverse = reverse * 10 + last_digit
#             number = number // 10

#         if original == reverse:
#             return True
#         else:
#             return False
