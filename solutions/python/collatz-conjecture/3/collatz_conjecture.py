def steps(number):

    """
    Calculate the number of steps to reach 1 using the Collatz Conjecture.
    
    :param number: A strictly positive integer.
    :return: The number of steps taken to reach 1.
    """

    if number <= 0 :
        raise ValueError("Only positive integers are allowed")
    
    else:
        steps = 0
        while number != 1 :
            if number % 2 == 0 :
                number = number // 2
            else :
                number = number * 3 + 1

            steps += 1
        return steps
