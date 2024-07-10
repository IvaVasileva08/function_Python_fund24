a = int(input())
b = int(input())
c = int(input())

def sum_numbers(a, b):
    sums = a + b
    return sums
def subtract(result, third):
    return result - third

def add_and_subtract(a, b, c):
    returned_result = sum_numbers(a, b)
    final_result = subtract(returned_result, c)
bimber = add_and_subtract(a, b, c)
print(bimber)
