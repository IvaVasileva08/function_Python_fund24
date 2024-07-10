a = int(input())
b = int(input())
c = int(input())
def smallest(a, b, c):
    min = a
    if b < a:
        min = b
    if c < a:
        min = c
    return min

min_num = smallest(a, b, c)
print(min_num)