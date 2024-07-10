numbers_as_string = input().split()
numbers_as_digits = []
def is_even(current_number):
    return current_number % 2 == 0
for number in numbers_as_string:
    numbers_as_digits.append(int(number))
final_list = list(filter(is_even, numbers_as_digits))
print(final_list)
