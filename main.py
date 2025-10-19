
def getInput():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    numbers = list(map(int, input().split()))
    return numbers

def makeReverse(numbers):
    """
    ########################################
    Code Your Program here
    ########################################
    """
    rev = [ numbers.pop() for _ in range(len(numbers)) ]
    return rev  

def main():
    numbers = getInput()
    ret = makeReverse(numbers)
    print(f'The result values are: {ret}')


if __name__ == '__main__':
    main()
