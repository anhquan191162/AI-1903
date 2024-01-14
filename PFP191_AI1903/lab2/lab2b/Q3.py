def validate_integer(value):
    try:
        int_value = int(value)
        return True, int_value
    except ValueError:
        return False, None

def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def reverse_number(number):
    return int(str(number)[::-1])

while True:
    user_input = input("Task 1: Enter an integer (n): ")
    is_valid, n = validate_integer(user_input)

    if is_valid:
        break
    else:
        print("Invalid input. Please enter an integer.")

binary_representation = bin(n)
print(f"Task 2: Binary representation of {n}: {binary_representation}")

n_for_sum = int(input("Task 3: Re-enter n (without input validation): "))
digit_sum = sum_of_digits(n_for_sum)
print(f"Task 3: Sum of digits of {n_for_sum}: {digit_sum}")

reverse_n = reverse_number(n_for_sum)
print(f"Task 4: Reverse of {n_for_sum}: {reverse_n}")
