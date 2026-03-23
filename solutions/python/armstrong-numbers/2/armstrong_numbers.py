def is_armstrong_number(number):
    number_str = str(number)
    exponent = len(number_str)
    total_sum = 0

    for digit in (number_str):
        total_sum += int(digit) ** int(exponent)

    return total_sum == number

print(is_armstrong_number(9))