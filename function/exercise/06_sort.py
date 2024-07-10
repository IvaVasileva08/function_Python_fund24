def sort_numbers():
    sequence = input()
    str_numbers = sequence.split()
    int_numbers = [int(num) for num in str_numbers]
    sorted_numbers = sorted(int_numbers)
    print (sorted_numbers)
sort_numbers()