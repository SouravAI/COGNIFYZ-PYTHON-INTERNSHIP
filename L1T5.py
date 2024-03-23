#Level 1 Task 5
def palindrome(s):
    s = s.replace(' ', '').lower()
    return s == s[::-1]

user_input = input("Enter a string: ")

if palindrome(user_input):
    print('TRUE, IT IS A PALINDROME')
else:
    print('FALSE, IT IS NOT A PALINDROME')


