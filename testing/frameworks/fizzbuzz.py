FIZZBUZZ = "FizzBuzz"
FIZZ = "Fizz"
BUZZ = "Buzz"


def fizzbuzz(i):
    """
    For multiples of three print “Fizz”, for the multiples of five print “Buzz”.
    For numbers which are multiples of both three and five print “FizzBuzz”. If none of
    above, print the number itself

    >>> fizzbuzz(9)
    'Fizz'
    >>> fizzbuzz(10)
    'Buzz'
    >>> fizzbuzz(75)
    'FizzBuzz'
    >>> fizzbuzz(17)
    17
    """
    if (i % 15) == 0:
        return FIZZBUZZ
    if (i % 3) == 0:
        return FIZZ
    if (i % 5) == 0:
        return BUZZ
    return i


def fizzbuzzlist(llist, sep):
    """
    Print items as a string separated by 'sep'. For multiples of three print “Fizz”, for the multiples of
    five print “Buzz”.For numbers which are multiples of both three and five print “FizzBuzz”. If none of
    above, print the number itself.
    >>> fizzbuzzlist([9,10,75], ',')
    'Fizz,Buzz,FizzBuzz'
    >>> fizzbuzzlist([2,3,4,5,6], '.')
    '2.Fizz.4.Buzz.Fizz'

    """
    op_list = []
    for i in llist:
        op_list.append(str(fizzbuzz(i)))
    return sep.join(op_list)


def show_me_exit(i):
    """
    example to demonstrate normal and abnormal exit
    exit with code passed

    """
    exit(i)  # Non-zero: abnormal exit, 0:successful exit


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
