def is_palindrome(number):
    return str(number) == str(number)[::-1]


while True:
    m = int(input("Enter the first integer (m): "))
    n = int(input("Enter the second integer (n, greater than m): "))

    if m < n:
        break
    else:
        print("Invalid input. Please ensure m < n.")


print(f"Palindrome numbers in the interval [{m}, {n}]:")
for num in range(m, n + 1):
    if is_palindrome(num):
        print(num)
