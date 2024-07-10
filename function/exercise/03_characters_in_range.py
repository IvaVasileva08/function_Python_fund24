first_chr = input()
second_chr = input()
def all_character(first_chr, second_chr):
    character = []
    for char_digit in range(ord(first_chr) +1, ord(second_chr)):
        character.append(chr(char_digit))
    return character
result = all_character(first_chr, second_chr)
print(" ".join(result))