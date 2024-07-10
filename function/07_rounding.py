"""a = float(input())
b = float(input())
c = float(input())
d = float(input())
def calculate(a, b, c, d):
    a1 = a.round()
    b1 = b.round()
    c1 = c.round()
    d1 = d.round()
answer = calculate(a, b, c, d)
print(f"{a} {b} {c} {d}")"""


def rounded_value(numbers):
    string_nums = numbers.split()
    rounded_list = []
    for nums in string_nums:
        number = float(nums)
        rounded_num = round(number)
        rounded_list.append(rounded_num)
    return rounded_list
input_string = input()
print(rounded_value(input_string))