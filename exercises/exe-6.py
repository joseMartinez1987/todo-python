# input = input('Enter a password')

# result = {
#     'len_password': False,
#     'has_number': False,
#     'has_capitalize_letter': False
# }


# if len(input) > 6:
#     len_password = True

# for letter in input:
#     if letter == letter.capitalize():
#         has_capitalize_letter = True
#         break
# for letter in input:
#     if letter.isdigit():
#         has_number = True
#         break

# if all(result.values()) :
#     print('Strong password')
# else:
#     print('The password do not meet the requirement!')


def test(a, b):
    try:
        print(f'a: {a}, b: {b}')
    except Exception as e:
        print('An error occurred')
        print(e)
test(b=2, a=1)
