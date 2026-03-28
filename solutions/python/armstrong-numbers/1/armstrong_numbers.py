def is_armstrong_number(number):
    d = str(number)
    digits = len(str(number))
    temp = 0
    temp2 = 0
    for i in range(digits):
        temp = int(d[i]) ** digits
        temp2 += temp

    if temp2 == number:
        return True
    else:
        return False
