
def get_number_length(num):
    length = 0
    
    while num != 0:
        length += 1
        num //= 10
    
    return length

def is_disarium_number(num):
    original_num = num
    length = get_number_length(num)
    sum = 0
    
    while num != 0:
        digit = num % 10
        sum += digit ** length
        length -= 1
        num //= 10
    
    return original_num == sum

n = int(input())

if is_disarium_number(n):
    print("True")
else:
    print("False")