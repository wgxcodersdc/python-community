from py.test import raises, main, mark
from fizzbuzz import fizzbuzz, fizzbuzzlist, show_me_exit
import sys


def test_fizzbuzz():
    assert fizzbuzz(9) == "Fizz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(75) == "FizzBuzz"

    assert fizzbuzz(7) == 7, "no fizz"
    assert fizzbuzz(17) == 17, "no buzz"
    assert fizzbuzz(75) == "FizzBuzz"


@mark.skipif(0, reason="I'd rather disable than fix")
def test_alpha():
    test = [9, 10, 75]

    assert fizzbuzzlist(test, ',') == 'Fizz,Buzz,FizzBuzz'


def test_charlie():
    test = list(range(2, 7))
    assert fizzbuzzlist(test, ',') == '2,Fizz,4,Buzz,Fizz'


def test_darwin():
    test = list(range(3, -5, -2))
    assert fizzbuzzlist(test, ',') == 'Fizz,1,-1,Fizz'


def test_type_error():
    with raises(TypeError):
        fizzbuzz("hello")


def test_exit():
    with raises(SystemExit) as e:
        show_me_exit(1)
    assert e.type == SystemExit
    assert e.value.code == 1


if __name__ == '__main__':
    main()
