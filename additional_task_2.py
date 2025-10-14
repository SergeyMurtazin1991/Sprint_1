def calculate_digital_root(number):
    summ = 0
    for digit in str(number):
        summ += int(digit)
    if summ > 9:
        summ = calculate_digital_root(summ)
    return summ

example1 = 4851
example2 = 97569
example3 = 889987
print(calculate_digital_root(example1))
print(calculate_digital_root(example2))
print(calculate_digital_root(example3))
