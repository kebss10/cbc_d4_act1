words = str(input("Input a word: "))

reverse = words.replace(" ", "")
palindrome = reverse[::-1]

if palindrome == reverse:
    print("This is a palindrome:", words)
else:
    print("This is not a palindrome:", words)
