import random

#function which generates character based on arguments passed
def get_char(char_list, number):
    temp_list = []
    for i in range (number):
        temp_list.append(random.choice(char_list))
    return temp_list

#input function
while True:
    num_char = int(input('Number of charecters in your Password: '))
    num_upper = int(input('Least Number of UPPERCASE in your Password: '))
    num_lower = int(input('Least Number of lowercase in your Password: '))
    num_digits = int(input('Least Number of Digits in your Password: '))
    num_sym = int(input('Least Number of Symbols in your Password: '))

    if num_char < num_digits+num_lower+num_upper+num_sym:
        print('The number of charecters are lesser then required')
    else:
        break


#different lists with indivisual functions
upper_list = [chr(i) for i in range(65,65+26)]
upper_char = get_char(upper_list,num_upper)

lower_list = [chr(i) for i in range(97,97+26)]
lower_char = get_char(lower_list,num_lower)

digit_list = [str(i) for i in range(0,10)]
digit_char = get_char(digit_list,num_digits)

sym_list = [chr(i) for i in range(33,48)]
sym_list +=[chr(i) for i in range (58,65)]
sym_list +=[chr(i) for i in range (91,97)]
sym_list +=[chr(i) for i in range (123,127)]
sym_char = get_char(sym_list,num_sym)

num_blank_char = num_char - num_upper - num_lower - num_digits - num_sym
full_list = upper_list + lower_list + digit_list + sym_list
fillers_char = get_char(full_list,num_blank_char)


#password Generation
password = upper_char + lower_char + digit_char + sym_char + fillers_char
random.shuffle(password)
password= "".join(password)

print(password)
