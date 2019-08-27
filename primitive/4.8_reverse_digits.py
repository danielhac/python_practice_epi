# Write a program which takes an integer and returns the integer 
# corresponding to the digits of the input written in reverse order. 

# For example, the reverse of 42 is 24, and the reverse of -314 is -413.


def reverse_digits(num):
    str_num = str(num)

    if str_num[0] == '-':
        return -int(''.join(str(e) for e in reversed(str_num.strip(str_num[0]))))
    else:
        return int(''.join(str(e) for e in reversed(str_num)))


print(reverse_digits(-123))
print(reverse_digits(123))
