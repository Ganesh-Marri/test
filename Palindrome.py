#palindrome number
num = input("Enter a number:")
if num == num[::-1]:
    print(f"{num} is a palidrome number")
else:
    print(f"{num} is not a palidrome number")
