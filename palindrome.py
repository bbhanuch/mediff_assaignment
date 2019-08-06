# Problem statement: Write a function that checks if a given word is a palindrome.
# Character case should be ignored.


def is_palindrome(input_string):
    reverse_string = (input_string[::-1])
    if input_string.lower() == reverse_string.lower():
        print "string is palindrome"
    else:
        print "string is not a palindrome"


input_string = str(input("Enter input string with quotes : "))
is_palindrome(input_string)