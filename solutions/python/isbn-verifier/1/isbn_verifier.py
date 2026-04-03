def is_valid(isbn):
    # Remove all hyphens
    isbn = isbn.replace("-", "")

    # Check if we have exactly 10 characters
    if len(isbn) != 10:
        return False

    # First 9 characters must be digits
    for char in isbn[:9]:
        if not char.isdigit():
            return False

    # 10th character must be a digit or 'X'
    if not (isbn[9].isdigit() or isbn[9] == 'X'):
        return False

    # Calculate the checksum
    total = 0
    for i, char in enumerate(isbn):
        if char == 'X':
            value = 10
        else:
            value = int(char)
        total += value * (10 - i)

    # Check if the total is divisible by 11
    return total % 11 == 0
