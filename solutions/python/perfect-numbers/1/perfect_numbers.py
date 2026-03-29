def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    else:
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)

        aliquot = 0

        for i in factors:
            aliquot += i
        aliquot = aliquot - number
        if aliquot == number:
            return 'perfect'
        elif aliquot <= number:
            return 'deficient'
        else:
            return 'abundant'

