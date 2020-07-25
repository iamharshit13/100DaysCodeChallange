#AMAZON GIFT CARD GENERATOR
import random
import string

def get_random_alphanumeric_string(letters_count, digits_count):
    sample_str = ''.join((random.choice(string.ascii_letters) for i in range(letters_count))).upper()
    sample_str += ''.join((random.choice(string.digits) for i in range(digits_count)))

    # Convert string to list and shuffle it to mix letters and digits
    sample_list = list(sample_str)
    random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    return final_string

a=1
number= int(input("How many coupon do you want to generate: "))
for i in range(number):
    tuning= random.randint(3,7)
    print(f"Coupon Code {a}:", get_random_alphanumeric_string(15-tuning, tuning))
    a+=1

# Just so that the command windows stays before you copy the copons.
imput()
