def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x1 = a % 10
    a = a //10
    x2 = a % 10
    a = a // 10
    x3 = a % 10
    a = a // 10
    x4 = a % 10
    a = a // 10
    x5 = a % 10
    return x5 > 0

print(main(1234))