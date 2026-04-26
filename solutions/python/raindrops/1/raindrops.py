def convert(number):
    if number % 3 == 0 or number % 5 == 0 or number % 7 == 0 :
        i = ""
        if number % 3 == 0:
            i += "Pling"
        if number % 5 == 0:
            i += "Plang"
        if number % 7 == 0:
            i += "Plong"

        return i
    else:
        return str(number)
