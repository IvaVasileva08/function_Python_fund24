def process_numbers():
    sequence = input()
    str_numbers = sequence.split()
    int_numbers = [int(num) for num in str_numbers]
    min_number = min(int_numbers)
    max_number = max(int_numbers)
    sum_numbers = sum(int_numbers)
    print(f"The minimum number is {min_number}")
    print(f"The maximum number is {max_number}")
    print(f"The sum number is: {sum_numbers}")
process_numbers()