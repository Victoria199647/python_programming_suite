"""
Generates Hailstone sequences (Collatz Conjecture) for any positive integer.
The sequence follows: if odd, multiply by 3 and add 1; if even, divide by 2.
"""


def main():
    """
    This program computes Hailstone sequences.
    When you type any positive integer, it will keep doing operations until the result is 1,
    and it will show how many operations have been done.
    If the number is odd, then it will *3+1
    If the number is even, then it will /2
    """
    print('This program computes Hailstone sequences.')
    number = int(input('Enter a number: '))
    # type the first number
    count = 0
    # count how many operations have been done
    
    while number > 1:
        is_odd = check_odd(number)
        # check if the number is odd or even, then choose the formula
        
        if is_odd:
            result1 = number * 3 + 1
            # odd number's formula
            print(str(number) + ' is odd, so I make 3n+1: ' + str(int(result1)))
            number = int(result1)
            # make the original number change to a new result number then re-enter the loop
        else:
            result2 = number / 2
            # even number's formula
            print(str(number) + ' is even, so I take half: ' + str(int(result2)))
            number = int(result2)
            # make the original number change to a new result number then reenter the loop
        
        count += 1
        # when ending the loop, it means operation add 1
    
    print('It took ' + str(count) + ' steps to reach 1.')


def check_odd(number):
    # check which formula to use
    if number % 2 == 1:
        return True
    return False


if __name__ == '__main__':
    main()
