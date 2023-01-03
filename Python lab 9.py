def check_palindrome(x):
    return x == x[::-1]

string = input("Enter a String : ")
result = check_palindrome(string)

if result:
    print(f"The Given string '{string}' is palindrome.")
else:
    print(f"The Given string '{string}' is not a palindrome.")
